#!/usr/bin/python3
"""This serves as the database engine for the project"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """This class defines the mysql database storage engine"""

    __engine = None
    __session = None

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
        """Gets all the instances of a given class or all instances if no class
        is provided
        """
        from models.engine.file_storage import classes

        subclasses = classes.copy()
        # deleting it because it does not inherit from `Base`
        if subclasses.get("BaseModel"):
            del subclasses["BaseModel"]

        if cls is None:
            return {
                f"{obj.__class__.__name__}.{obj.id}": obj
                for c in subclasses.values()
                for obj in self.__session.query(c).all()
            }

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
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the database session"""
        self.__session.close()
