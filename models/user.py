#!/usr/bin/python3
"""Class user that inherites from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines the data of an user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
