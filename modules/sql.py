from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HistoryQuiz(Base):
    __tablename__ = 'historyquiz'
    quiz_id = Column(Integer,primary_key=True)
    question = Column(String,nullable=True)
    answer = Column(String,nullable=True)