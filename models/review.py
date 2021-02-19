#!/usr/bin/python3
"""Class Review that inherites from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that defines the reviews"""

    place_id = ""
    user_id = ""
    text = ""
