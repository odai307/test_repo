#!/usr/bin/python3
"""
Base model for object serialization, deserialization,
seve to file, retrieving from file, whic happens as used by other models
"""

import uuid
from datetime import datetime


class BaseModel():
    """Base model class for the project"""
    id = None
    created_at = None
    updated_at = None

    def __init__(self) -> None:
        """constructor for the object"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
