#!/usr/bin/env python3
"""
Module `user` defines the class `User` and all functions needed to interact
with the User model.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()


class User(Base):
    """
    `User` class defines the SQLAlchemy model for a user.
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
