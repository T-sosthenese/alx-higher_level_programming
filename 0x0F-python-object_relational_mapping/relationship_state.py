#!/usr/bin/python3
"""
Modeling a class definition of the state.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from relationship_city import Base, City

Base = declarative_base()


class State(Base):
    """
    A class that inherits from the base declarative class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
