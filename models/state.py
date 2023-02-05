#!/usr/bin/python3
"""This is the state class"""
import os
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

engines = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    if engines == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')

    else:
        name = ""

        @property
        def cities(self):
            """Getter method for cities
            Return: list of cities with state_id equal to self.id
            """
            # return list of City objs in __objects
            cities_dict = models.storage.all(City).values()
            cities_list = []
            # append city from dict values to list
            [
                cities_list.append(city)
                for city in cities_dict.keys()
                if city == self.id
            ]
            return cities_list
