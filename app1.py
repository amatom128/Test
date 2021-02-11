from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import io
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app,resource={r"/api/*":{"origins":"*"}})

@app.route('/api')
def home():
    return render_template("index.html")

@app.route('/api/csv',methods=["POST"])
def upload():
    f = request.files['myfile']
    print(f)
    if not f:
        return "No File"

    stream = io.StringIO(f.stream.read().decode("UTF8"),newline=None)
    csv_input = csv.reader(stream)
    print(csv_input)
    for row in csv_input:
        print(row)

    return render_template("index.html")
    
if __name__ == "__main__":
    app.run()