#!/usr/bin/python3
"""Amenity Module for HBNB project"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """The Amenity class"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary='place_amenity', viewonly=False
    )
