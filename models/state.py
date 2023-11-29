#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(60), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    def cities(self):
        """ Getter attribute, return the lisst of citu instance in state.id """
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
