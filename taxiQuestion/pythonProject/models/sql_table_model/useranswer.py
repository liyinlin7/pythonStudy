from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserAnswer(Base):
    __tablename__ = 'useranswer'

    question_id = Column(String(255), primary_key=True, nullable=False )
    user_answer = Column(String(45), nullable=False)
    answer_bool = Column(Integer, nullable=False)
    useranswer_key = ["question_id", "user_answer", "answer_bool"]

