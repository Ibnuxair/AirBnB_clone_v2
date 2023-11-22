#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """ Initializes the attributes. """
        self.id = str(uuid.uuid4())

        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'updated_at' in kwargs and 'created_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                del kwargs['__class__']
                self.__dict__.update(kwargs)
            else:
                # Handle missing 'updated_at' or 'created_at' keys
                self.created_at = kwargs.get('created_at', datetime.now())
                self.updated_at = kwargs.get('updated_at', datetime.now())

        # If it's a new instance, add a call to the new method on storage
        from models import storage
        storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        obj_dict = {
            k: v for k, v in self.__dict__.items() if k in self.__dict__
            and v != ''
        }
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, obj_dict)

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
