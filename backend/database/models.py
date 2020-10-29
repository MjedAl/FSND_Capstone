import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

# Uncomment when you want to use real database
# DB_HOST = os.getenv('DB_HOST')
# DB_USER = os.getenv('DB_USER')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_NAME = os.getenv('DB_NAME')
# DB_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER,
#                                                             DB_PASSWORD,
#                                                             DB_HOST,
#                                                             DB_NAME)

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
DB_URI = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple
     verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


# Relation between Actor and Movies is Many-To-Many so we need a thrid table to
#  control their relation
ActorInMovie = db.Table('ActorInMovie',
                        db.Column('actor_id',
                                  db.Integer,
                                  db.ForeignKey('actor.id'),
                                  primary_key=True),
                        db.Column('movie_id',
                                  db.Integer,
                                  db.ForeignKey('movie.id'),
                                  primary_key=True)
                        )


class Movie(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True)
    release_date = Column(String(80), nullable=False)
    poster_link = db.Column(db.String(500))
    actors = db.relationship("Actor",
                             secondary=ActorInMovie,
                             cascade='all, delete')

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
    age = Column(String(80), nullable=False)
    image_link = db.Column(db.String(500))
    gender = Column(String(10), nullable=False)

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
