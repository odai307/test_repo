#!/usr/bin/python3
"""City Location of the houses
"""
from base_model import BaseModel


class City(BaseModel):
    """Class representation of the city
    """
    state_id:str = ""
    name:str = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """ constructor for the city
        """
