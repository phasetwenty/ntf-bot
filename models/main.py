# Copyright 2019 Christopher Haverman
# All Rights Reserved
#
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'Christopher Haverman'

Base = declarative_base()


class Leaderboard(Base):
    __tablename__ = 'Leaderboard'

    id = Column(Integer, primary_key=True)
    match = Column(Text)
    place = Column(Integer)
