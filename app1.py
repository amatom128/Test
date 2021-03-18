from flask import Flask,render_template,request,redirect, url_for
from flask_cors import CORS
from modules.sql import HistoryQuestion,HistoryAnswer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import io
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app,resource={r"/api/*":{"origins":"*"}})

@app.route('/home',methods=['GET'])
def home():
    return render_template("index.html")

'''
class HistoryQuiz(Base):
    __tablename__ = 'historyquiz'
    quiz_id = Column(Integer,primary_key=True)
    question = Column(String,nullable=True)
    answer = Column(String,nullable=True)
'''

@app.route('/api/csv',methods=["POST"])
def upload():


    f = request.files['myfile'] 
    print(f)
    if not f:
        return "No File"

    stream = io.StringIO(f.stream.read().decode("UTF8"))
    csv_input = csv.reader(stream)
    #verify duplicate questions
    try:
        for row in csv_input:
            question = row[0]
            list_answers = row[1].split(",")
            #print(list_answers)
            question = HistoryQuestion(question=row[0])
            for ele in list_answers:
                print(ele)
            #     answer = HistoryAnswer(answer=row[1])
            db.session.add(question)


            db.session.commit()

        db.session.close()

    except Exception as e:
        print("Error: ",e)
  

    return redirect(url_for('home'))


@app.route('/api/play',methods=["GET"])
def play():
    pass


if __name__ == "__main__":
    app.run()