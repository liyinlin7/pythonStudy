from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Paper(Base):
    __tablename__ = 'paper'

    paperId = Column(String(255), primary_key=True, nullable=False)
    paperName = Column(String(255), nullable=False)
    paperType = Column(String(255), nullable=False)
    paperRange = Column(String(255), nullable=False)
    paperQuestionType = Column(String(255), nullable=False)
    createTime = Column(DateTime, nullable=False)



