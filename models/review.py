#!/usr/bin/python3
"""modelling the reviews on the various apartments
"""
from base_model import BaseModel


class Review(BaseModel):
    """class representation on the reviews made on the apartments
    """
    place_id:str = ""
    user_id:str = ""
    text:str = ""