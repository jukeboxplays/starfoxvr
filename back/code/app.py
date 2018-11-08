from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from flask_restful import Resource, Api
from config import Config
from flask_migrate import Migrate
from datetime import datetime
import sys
import time

'''
EXEMPLO:
https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
'''

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
db = SQLAlchemy(app)

'''
API
'''
class HelloWorld(Resource):
    def get(self):
        #test()
        return {'hello': 'world'}
    
    def post(self):
        content = request.get_json()
        return content

class Register(Resource):
    def post(self):
        content = request.get_json()
        obj = Users(username=content['username'],
                   email=content['email'],
                   password_hash=content['password'])
        r = add_to_db(obj)
        return r
    
api.add_resource(HelloWorld, '/api/v1/')
api.add_resource(Register, '/api/v1/register')


'''
DATABASE CLASSES
'''
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
class Film(db.Model):  
    # Row definitions
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    director = db.Column(db.String)
    year = db.Column(db.String)
    

'''
DB CONNECTIONS
'''

# ======
# TESTES
# ======

# BANCO
def add_to_db(obj):
    # Create 
    db.session.add(obj)  
    db.session.commit()
    return "Adicionado"


    
def read_from_db(name=None):
    # Read
    if name:
        films = db.session.query(Film).filter(Film.title == name)
    else:
        films = db.session.query(Film)
    return films

def update_row(row, new_name):
    # Update
    row.title = new_name  
    db.session.commit()

def delete_row(row):
    # Delete
    db.session.delete(row)  
    db.session.commit()

def test():
     obj = Film(title="Doctor Strange", director="Scott Derrickson", year="2016")
     add_to_db(obj)

     obj = Film(title="Spoderman", director="Jack Nicholson", year="2010")
     add_to_db(obj)

     print("eita")
     films = read_from_db()
     for film in films:
         print (film.title)
     print("lsl")
         
     films = read_from_db("Spoderman")
     update_row(films[0], "Gorilas")

     delete_row(films[0])

time.sleep(3)
db.create_all()
