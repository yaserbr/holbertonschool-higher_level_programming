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
    new_data = State(name="Louisiana")
    s.add(new_data)
    s.commit()
    print(new_data.id)
