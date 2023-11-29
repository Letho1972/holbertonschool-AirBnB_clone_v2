#!/usr/bin/python3
"""
This is the DBStorage class for AirBnB
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of DBStorage class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(getenv('HBNB_MYSQL_USER'),
                                   getenv('HBNB_MYSQL_PWD'),
                                   getenv('HBNB_MYSQL_HOST'),
                                   getenv('HBNB_MYSQL_DB')
                            ), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """ Query on the current database session """
        query_objects = {}
        _class = [User, State, City, Amenity, Place, Review]

        if cls is None:
            for cls in _class:
                for key in self.__session.query(cls):
                    storage["{}.{}".format(cls.__name__, instance.id)] = key
        else:
            for cls in _class:
                for key in self.__session.query(cls):
                    storage["{}.{}".format(cls.__name__, instance.id)] = key

        result = {obj.__class__.__name__ + "." + obj.id: obj for obj in query_objects}

        return result

    def new(self, obj):
        """ Add a new object """
        self.__session.add(obj)

    def save(self):
        """ save the instance """
        self.__session.commit()

    def delete(self, obj=None):
        """ del an object of an instance """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ lunch a new instance """

        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        self.__session = scoped_session(Session)
