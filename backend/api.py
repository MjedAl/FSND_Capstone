import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Movie, Actor
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)



@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors():
    try:
        actors = Actor.query.all()
        return jsonify({
            'success': True,
            'drinks': [actor.short() for actor in actors]
        })
    except Exception:
        abort(500)

@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies():
    try:
        movies = Movie.query.all()
        return jsonify({
            'success': True,
            'drinks': [movie.short() for movie in movies]
        })
    except Exception:
        abort(500)

@app.route('/movies/<movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(movie_id):
    try:
        movie = Movie.query.filter_by(id=movie_id).one_or_none()
        if movie is None:
            abort(404)
        movie.delete()
        return jsonify({
            'success': True
        })
    except Exception:
        abort(500)

@app.route('/actors/<actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(actor_id):
    try:
        actor = Actor.query.filter_by(id=actor_id).one_or_none()
        if actor is None:
            abort(404)
        actor.delete()
        return jsonify({
            'success': True
        })
    except Exception:
        abort(500)

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def post_actors(payload):
    JSON_body = request.get_json()
    name = JSON_body.get('name')
    age = JSON_body.get('age')
    image_link = JSON_body.get('image_link')
    gender = JSON_body.get('gender')

    actor = Actor(name=name, age=age, image_link=image_link, gender=gender)
    actor.insert()
    return jsonify({
        'success': True,
        'actor': actor.id
        })

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def post_movie(payload):
    JSON_body = request.get_json()
    title = JSON_body.get('title')
    release_date = JSON_body.get('release_date')
    poster_link = JSON_body.get('poster_link')

    movie = Movie(title=title, poster_link=poster_link, release_date=release_date)
    movie.insert()
    return jsonify({
        'success': True,
        'movie': movie.id
        })

# TODO PATCH /actors/ and /movies/


# Error Handling


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
    }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
    }), 404


@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Un-processable Entity"
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
    }), 500

'''
@implement error handler for AuthError CHANGE
    error handler should conform to general task above
'''


@app.errorhandler(AuthError)
def auth_error(exception):
    """
    Receive the raised authorization error and propagates it as response
    """
    return jsonify(exception.error), exception.status_code