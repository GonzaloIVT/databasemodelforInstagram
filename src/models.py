import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario1(Base):
    __tablename__ = 'Usuario1'
    nickname = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mail= Column(String(50))
    password= Column(String(20))
    dob = Column(Integer)
    relacionPost1 = relationship("Post1")
    relacionComment1 = relationship("Comment1")

class Post1(Base):
    __tablename__ = 'Post1'
    Id = Column(Integer, primary_key=True)
    name = Column(String(50), ForeignKey('Usuario1.nickname'), nullable=False)
    Conten= Column(String(400))
    date= Column(Integer)
    ubication = Column(String(20))
    Comment = Column(String(300), ForeignKey("Comment2.name"))

class Comment1(Base):
    __tablename__ = 'Comment1'
    Id = Column(Integer, primary_key=True)
    name = Column(String(50), ForeignKey('Usuario1.nickname'), nullable=False)
    Conten= Column(String(50))
    date= Column(Integer)
    etiqueta = Column(String(10))
    relacionPostUser2 = relationship("Post2")

class Usuario2(Base):
    __tablename__ = 'Usuario2'
    nickname = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mail= Column(String(50))
    password= Column(String(20))
    relacionPost2 = relationship("Post2")
    relacionComment2 = relationship("Comment2")

class Post2(Base):
    __tablename__ = 'Post2'
    Id = Column(Integer, primary_key=True)
    name = Column(String(50), ForeignKey('Usuario2.nickname'), nullable=False)
    Conten= Column(String(400))
    date= Column(Integer)
    ubication = Column(String(20))  
    Comment = Column(String(300), ForeignKey("Comment1.name"))
    

class Comment2(Base):
    __tablename__ = 'Comment2'
    Id = Column(Integer, primary_key=True)
    name = Column(String(50), ForeignKey('Usuario2.nickname'), nullable=False)
    Conten= Column(String(50))
    date= Column(String(20))
    etiqueta = Column(String(10))
    relacionPostUser1 = relationship("Post1")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e