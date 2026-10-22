#!/usr/bin/python3
"""List all states from the database using SQLAlchemy."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    session = sessionmaker(bind=engine)
    s = session()
    q = s.query(State).order_by(State.id).first()
    if q is not None:
        print("{}: {}".format(q.id, q.name))
    else:
        print("Nothing")
    s.close()
