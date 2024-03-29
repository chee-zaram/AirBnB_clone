#!/usr/bin/python3
"""This serves as the database engine for the project"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
import inspect
from models.engine.file_storage import FileStorage


class DBStorage:
    """This class defines the mysql database storage engine"""

    __engine = None
    __session = None
    __classes = FileStorage().classes.copy()
    if __classes.get("BaseModel"):
        del __classes["BaseModel"]

    def __init__(self):
        """Constructor for the storage session"""

        uname = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", "localhost")
        port = getenv("HBNB_MYSQL_PORT", "3306")
        database = getenv("HBNB_MYSQL_DB")

        url = f"mysql+mysqldb://{uname}:{passwd}@{host}:{port}/{database}"
        self.__engine = create_engine(url, pool_pre_ping=True, echo=False)

        if getenv("HBNB_MYSQL_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Gets all the instances of a given class or all instances if no class
        is provided
        """

        if cls is None:
            return {
                f"{obj.__class__.__name__}.{obj.id}": obj
                for c in self.__classes.values()
                for obj in self.__session.query(c).all()
            }

        if cls not in self.__classes and cls.__name__ not in self.__classes:
            raise TypeError("{} is not a valid class".format(cls))

        if not inspect.isclass(cls):
            cls = self.__classes[cls]

        return {
            f"{obj.__class__.__name__}.{obj.id}": obj
            for obj in self.__session.query(cls)
        }

    def new(self, obj):
        """Adds a new object to the database session"""
        from models.base_model import BaseModel

        if not isinstance(obj, BaseModel):
            return

        try:
            self.__session.add(obj)
            self.__session.flush()
            self.__session.refresh(obj)
        except Exception as e:
            self.__session.rollback()
            raise e

    def save(self):
        """Saves changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an instance from the database"""
        from models.base_model import BaseModel

        if not isinstance(obj, BaseModel):
            return

        self.__session.delete(obj)

    def reload(self):
        """Reloads objects from the database"""

        Base.metadata.create_all(self.__engine, checkfirst=True)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Closes the database session"""
        self.__session.remove()

    def get(self, cls, id):
        """Gets an object of type `cls` with given `id` in database storage"""
        if cls not in self.__classes and cls not in self.__classes.values():
            raise TypeError("{} is not a valid class".format(cls))

        if type(id) != str:
            raise TypeError("{} must be a string".format(id))

        if type(cls) == str:
            cls = self.__classes[cls]

        return next((obj for obj in self.all(cls).values() if obj.id == id),
                    None)

    def count(self, cls=None):
        """Gets the number of objects of type `cls` in database storage"""
        if cls is None:
            return len(list(self.all().values()))

        if cls not in self.__classes and cls not in self.__classes.values():
            raise TypeError("{} is not a valid class".format(cls))

        if type(cls) == str:
            cls = self.__classes[cls]

        return len(list(self.all(cls).values()))
