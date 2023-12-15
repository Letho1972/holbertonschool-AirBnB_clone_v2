#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """
    This class manages storage of hbnb models in a database
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new DBStorage instance
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db = getenv('HBNB_MYSQL_DB')

        db_url = f'mysql+mysqldb://{user}:{password}@{host}/{db}'

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

        # Thread-local session to avoid issues when multithreading
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """
        Returns a dictionary of all the objects, or only from the given
        class if cls is specified.
        """

        classes = [User, State, City, Amenity, Place, Review]
        storage = {}

        if cls is None:
            for cls in classes:
                for instance in self.__session.query(cls).all():
                    storage[f"{cls.__name__}.{instance.id}"] = instance
        else:
            if cls in classes:
                for instance in self.__session.query(cls).all():
                    storage[f"{cls.__name__}.{instance.id}"] = instance

        return storage

    def new(self, obj):
        """Adds the given object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes the given object from the current database session
        (if not None)
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and initializes the session"""

        Base.metadata.create_all(self.__engine)

        # Thread-local session to avoid issues when multithreading
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        self.__session.remove()
