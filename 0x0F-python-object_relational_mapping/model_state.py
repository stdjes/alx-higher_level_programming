#!/usr/bin/python3
"""Module For Base and State Classes for SQLAlchemy"""

from sqlalchemy import MetaData, Column, INT, String
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """State Class links to the MySQL table states"""
    __tablename__ = 'states'
    id = Column(INT, nullable=False, unique=True,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
