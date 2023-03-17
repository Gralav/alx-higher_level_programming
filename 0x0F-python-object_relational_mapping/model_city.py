#!/usr/bin/python3
""" Script that contains the class definition of a City and an instance
    Base = declarative_base() """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State
Base = declarative_base()


class City(Base):
    """ Defining class cities """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
