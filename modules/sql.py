from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class HistoryAnswer(Base):
    __tablename__ = 'historyanswer'
    id = Column(Integer,primary_key=True)
    question_id = Column(Integer,ForeignKey("historyquestion.id"))
    answer = Column(String)
    
    

class HistoryQuestion(Base):
    __tablename__ = 'historyquestion'
    id = Column(Integer,primary_key=True)
    question = Column(String,unique=True)
    roles = relationship("HistoryAnswer")


'''
create table historyanswer ( 
      id INTEGER NOT NULL PRIMARY KEY,        
      question_id INTEGER,
      answer TEXT,
      FOREIGN KEY(question_id) REFERENCES historyquestion (id)
     );   

CREATE TABLE historyquestion ( 
    id INTEGER NOT NULL PRIMARY KEY,
    question TEXT
    );     

'''
'''
HistoryAnswer(answer=answer,question=HistoryQuestion.id)
'''


    