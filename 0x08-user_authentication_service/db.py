#!/usr/bin/env python3
"""
Module for db.py
0x08. User authentication service
Holberton Web Stack programming Spec ― Back-end
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User
        

class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Defines an user instance and saves it to the database

        Args:
        ----
            email: user's email
            hashed_password:  user's password
        Returns:
        -------
            `User` object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs):
        """ Documentation for this method """
        if not kwargs:
            raise InvalidRequestError
        if not all(key in User.__table__.columns for key in kwargs):
            raise InvalidRequestError
        row = self._session.query(User).filter_by(**kwargs).first()
        if not row:
            raise NoResultFound
        return row

    def update_user(self, user_id: int, **kwargs):
        """ Documentation for this method """
        # check cause changed:
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if not hasattr(user, key):
                    raise ValueError
                setattr(user, key, value)
            self._session.commit()
        except NoResultFound:
            pass
        finally:
            return None
