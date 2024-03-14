from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from models.sql_table_model.questions import Questions

Base = declarative_base()

class UserAnswer(Base):
    __tablename__ = 'useranswer'

    id = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(String(255), ForeignKey('questions.question_id'), nullable=False )
    user_answer = Column(String(45), nullable=False)
    answer_bool = Column(Integer, nullable=False)
    # 关系属性，反向指向  Question
    # question = relationship( "Question" )
    question = relationship( "Questions",  uselist=False, back_populates="user_answer" )

