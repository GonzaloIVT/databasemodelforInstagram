import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    nickname = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mail= Column(String(50))
    password= Column(String(20))
    dob = Column(Integer)
    relacionPost1 = relationship("Post")
    relacionComment = relationship("Comment")
    relacionFollowers = relationship("Followers")

class Post(Base):
    __tablename__ = 'Post'
    Id = Column(Integer, primary_key=True)
    name = Column(String(50), ForeignKey('Usuario.nickname'), nullable=False)
    Conten= Column(String(400))
    date= Column(Integer)
    ubication = Column(String(20))
    relacionMedia = relationship("Media")
    relacionCommentA = relationship("Comment")

class Comment(Base):
    __tablename__ = 'Comment'
    Id = Column(Integer, primary_key=True)
    author_id= Column(String(50), ForeignKey('Usuario.nickname'), nullable=False)
    Conten= Column(String(50))
    post_id= Column(String(50), ForeignKey('Post.Id'), nullable=False)
    

class Followers(Base):
    __tablename__ = 'Followers'
    User_from_id = Column(Integer, primary_key=True)
    User_to_id = Column(Integer, ForeignKey('Usuario.nickname'), nullable=False)
    
    

class Media(Base):
    __tablename__ = 'Media'
    Id = Column(Integer, primary_key=True)
    name = Column(String(50))
    url= Column(String(400))
    post_id= Column(Integer , ForeignKey('Post.Id'), nullable=False)
    tipo= Column(String(20))  
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e