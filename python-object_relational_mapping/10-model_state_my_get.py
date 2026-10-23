#!/usr/bin/python3
"""List all states from the database using SQLAlchemy."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    en = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    session = sessionmaker(bind=en)
    s = session()
    target = sys.argv[4]
    data = s.query(State).where(State.name == target).first()
    if data is not None:
        print(data.id)
    else:
        print("Not found")
