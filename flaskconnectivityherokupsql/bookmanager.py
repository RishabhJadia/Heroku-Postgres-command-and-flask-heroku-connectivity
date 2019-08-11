from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from flask_heroku import Heroku  #used for production server


app = Flask(__name__)
app.secret_key = "super secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/mybooks'  # used for local server

# postgresql = database (it can be mysql, sqlite etc)
# postgres = user name (which will created manually)
# password = user password (if not there is no password leave it blank)
# localhost = localhost
# mybooks = table name (which will created manually)

# heroku = Heroku(app) #used for production server when using local sever
# comment this line and vice-versa
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    contact = db.Column(db.Integer)

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __repr__(self):
        return '<User %r>' % self.name

# after this now cross check our database is working correctly or not by using 
# following in terminal
# 1.type python3
# 2.type from bookmanager import db
# 3.type db.create_all()
# 4.last check on database our table is created or not


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        reg = Books(request.form['name'], request.form['contact'])
        db.session.add(reg)
        db.session.commit()
        return render_template('home.html')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
