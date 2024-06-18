from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class PaperQuestion(Base):
    __tablename__ = 'paper_questions'

    paper_id = Column(String(255), nullable=False)
    question_id = Column(String(45), nullable=False)
    question_answer = Column(String(45))
    user_answer = Column(String(45))
    question_bool = Column(String(45))

