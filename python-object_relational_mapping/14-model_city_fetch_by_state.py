#!/usr/bin/python3
"""List all cities with their state names using SQLAlchemy."""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    sessionn = sessionmaker(bind=engine)
    s = sessionn()
    data = (
        s.query(State, City)
        .join(State, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )
    for row in data:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
    s.close()
