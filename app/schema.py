from sqlalchemy import *
from database import Base

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer,primary_key = True)
    name = Column(String)
    def __init__(self,id,name):
        self.id = id
        self.name = name

