#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            cls_dict = {}  # create empty dict to store classes
            for key,value in FileStorage.__objects.items():
                # print(cls)
                # ==> if item class in __object matches cls
                if type(value) is cls:
                    # print(FileStorage.__objects[key])
                    # ==> save to cls_dict
                    cls_dict[key] = value
            return cls_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes a given object from __objects if it exists"""
        try:  # ==> use try block to avoid errors
            # ==> create object key using class_name and objet id
            obj_key = f"{type(obj).__name__}.{obj.id}"
            # print(obj_key)
            # print(self.__objects)
            # ==> delete instance from __objects dict passing the object key
            del self.__objects[obj_key]
            # ==> save the updated __object
            FileStorage.save()
        except Exception:
            pass
