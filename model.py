from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_heroku import Heroku


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
heroku = Heroku(app)
db = SQLAlchemy(app)


# Create our database model
class Story(db.Model):
    __tablename__ = "Story"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    Stort= db.Column('content', db.String)

    def __init__(self, name, content):
        self.name = name
        self.content = content



class User(db.Model):
    __tablename__="User"
    id=db.Column('id',db.Integer, primary_key=True)
    email=db.Column('email',db.String)
    Name=db.Column('Name',db.String)
    password=db.Column('password',db.Integer)
    def __init__(self, email, Name, password):
        self.email = email
        self.Name = Name
        self.password= password


class Review(db.Model):
    """docstring for ClassName"""
    __tablename__="Review"
    id=db.Column('id',db.Integer, primary_key=True)
    name=db.Column('name',db.String)
    review=db.Column('revirew',db.String)
    def __init__(self, name,revirew):
        self.name = name
        self.revirew = revirew
        

#db.create_all()

if __name__ == '__main__':
    db.session.query(Story).delete()
    story=Story(name='HP', cont='asdsf')
    db.session.add(story)
    story=Story(name='H1P', cont='as4tf4rdsf')
    db.session.add(story)

    db.session.commit()

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)