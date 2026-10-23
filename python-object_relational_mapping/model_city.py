#!/usr/bin/python3
"""Define the State model for the states table using SQLAlchemy."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represent a state stored in the MySQL states table."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
