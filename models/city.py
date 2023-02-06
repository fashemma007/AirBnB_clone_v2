#!/usr/bin/python3
"""This is the city class"""
import models
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


storage_engine = os.environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    if (storage_engine == "db"):
        # initialize class for file/db storage type
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='cities')
    else:
        name = ""
        state_id = ""
