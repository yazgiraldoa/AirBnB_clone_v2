#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship(
        "Review",
        backref="place",
        cascade="all, delete, delete-orphan")

    @property
    def reviews(self):
        """ Getter that that returns the list of Reviews instances """
        review_instances = models.storage.all(Review)
        new_list = []
        for value in review_instances.values():
            if value.place_id == (self.id):
                new_list.append(value)
        return (new_list)
