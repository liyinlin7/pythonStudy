from sqlalchemy import Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Questions(Base):
    __tablename__ = 'questions'

    question_id = Column(String(255), primary_key=True, nullable=False)
    question_answer = Column(String(16), nullable=False)
    question_title = Column(String(255), nullable=False)
    correct_answer = Column(String(255), nullable=False)
    question_type = Column(Integer, nullable=False)
    range = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    collect = Column(Integer, nullable=False, server_default=text("1"))

