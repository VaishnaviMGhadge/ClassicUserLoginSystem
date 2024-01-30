from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,Column,String




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='dontgiveafk'
db = SQLAlchemy(app)



class User(db.Model,UserMixin):
    id=Column(db.Integer,primary_key=True)
    name=Column(db.String(30),primary_key=True,nullable=False,unique=True)
    password=Column(db.String(80),nullable=False)


