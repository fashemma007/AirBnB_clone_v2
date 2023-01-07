#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        """Getter method for cities
        Return: list of cities with state_id equal to self.id
        """
        # return list of City objs in __objects
        cities_dict = storage.all(City)
        cities_list = []

        # copy values from dict to list
        for value in cities_dict.keys():
            cities_list.append(value)

        return cities_list
