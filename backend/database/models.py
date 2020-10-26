import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'admin')
DB_NAME = os.getenv('DB_NAME', 'capstone')
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER,
                                                            DB_PASSWORD,
                                                            DB_HOST,
                                                            DB_NAME)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Drink
a persistent drink entity, extends the base SQLAlchemy Model
'''
class Movie(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True)
    release_date =  Column(String(80), nullable=False)
    poster_link = db.Column(db.String(500))
    actors = db.relationship('Actor', backref='movie')

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())

class Actor(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    age =  Column(String(80), nullable=False)
    image_link = db.Column(db.String(500))
    gender =  Column(String(10), nullable=False)
    movies = db.relationship('Movie', backref='actor')

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
