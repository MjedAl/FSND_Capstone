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


db_drop_and_create_all()


@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors(payload):
    try:
        actors = Actor.query.all()
        if actors is None:
            abort(404)
        return jsonify({
            'success': True,
            'actors': [actor.short() for actor in actors]
        })
    except Exception:
        abort(500)


@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies(payload):
    try:
        movies = Movie.query.all()
        if movies is None:
            abort(404)
        return jsonify({
            'success': True,
            'movies': [movie.short() for movie in movies]
        })
    except Exception as e:
        abort(500)


@app.route('/movies/<movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(payload, movie_id):
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
def delete_actors(payload, actor_id):
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
        'actor_id': actor.id
        })


@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def post_movie(payload):
    JSON_body = request.get_json()
    title = JSON_body.get('title')
    rel_date = JSON_body.get('release_date')
    pos_link = JSON_body.get('poster_link')

    movie = Movie(title=title, poster_link=pos_link, release_date=rel_date)
    movie.insert()
    return jsonify({
        'success': True,
        'movie_id': movie.id
        })


@app.route('/actors/<actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actor(payload, actor_id):
    actor = Actor.query.get(actor_id)
    if actor is None:
        abort(404)
    else:
        JSON_body = request.get_json()
        name = JSON_body.get('name')
        age = JSON_body.get('age')
        image_link = JSON_body.get('image_link')
        gender = JSON_body.get('gender')
        if name is not None:
            actor.name = name
        if age is not None:
            actor.age = age
        if image_link is not None:
            actor.image_link = image_link
        if gender is not None:
            actor.gender = gender
        actor.update()
        return jsonify({
            'success': True,
            'actor': actor.short()
        })


@app.route('/movies/<movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movies(payload, movie_id):
    movie = Movie.query.get(movie_id)
    if movie is None:
        abort(404)
    else:
        JSON_body = request.get_json()
        title = JSON_body.get('title')
        release_date = JSON_body.get('release_date')
        poster_link = JSON_body.get('poster_link')
        if title is not None:
            movie.title = title
        if release_date is not None:
            movie.release_date = release_date
        if poster_link is not None:
            movie.poster_link = poster_link
        movie.update()
        return jsonify({
            'success': True,
            'movie': movie.short()
        })

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
