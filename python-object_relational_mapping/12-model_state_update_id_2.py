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
    qdata = s.query(State).where(State.id == 2).first()
    qdata.name = "New Mexico"
    s.commit()
