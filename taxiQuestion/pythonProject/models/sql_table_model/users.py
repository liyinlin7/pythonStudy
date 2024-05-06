from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    userid = Column(String(255), primary_key=True, nullable=False)
    user_name = Column(String(255))
    password = Column(String(255), nullable=False)
    user_phone = Column(String(255), nullable=False)

