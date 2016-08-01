from sqlalchemy import *
from database import Base

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer,primary_key = True)
    name = Column(String)
    def __init__(self,id,name):
        self.id = id
        self.name = name
       
class SSR(Base):
    __tablename__="ssr"
    id = Column(Integer,primary_key = True)
    reel_name = Column(String)
    seq_name = Column(String)
    shot_name = Column(String)

    def __init__(self,id,reel,seq,shot):
        self.id = id
        self.reel_name = reel
        self.seq_name = seq
        self.shot_name = shot
