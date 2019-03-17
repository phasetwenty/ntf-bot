# Copyright 2019 Christopher Haverman
# All Rights Reserved
#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

__author__ = 'Christopher Haverman'


def start():
    engine = create_engine('sqlite:////Users/Chris/Workspace/repos/ntf-bot/ntf-bot.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
