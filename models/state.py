#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete",
        passive_deletes=True)

    @property
    def cities(self):
        """ Getter that that returns the list of City instances """
        cities_instances = models.storage.all(City)
        new_list = []
        for value in cities_instances.values():
            if value.state_id == (self.id):
                new_list.append(value)
        return (new_list)
