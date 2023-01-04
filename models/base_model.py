#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        if not kwargs:  # if no dictionary (key&value) argument is passed
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.__set_from_dict(**kwargs)
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __set_from_dict(self, **kwargs):
        """Private method that creates a new instance from dict args"""
        for k, v in kwargs.items():
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
            if k != "__class__":
                if k in ("created_at", "updated_at"):
                    # Construct a date from the output of date.isoformat()
                    # setattr(x, 'y', v) is equivalent to x.y = v where;
                    # x is dict_name, y is the key and v is the value
                    setattr(self, k, datetime.fromisoformat(v))
                # otherwise create a key and value pair of other attributes
                else:
                    setattr(self, k, v)
