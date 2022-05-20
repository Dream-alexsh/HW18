from flask import request
from flask_restx import Resource, Namespace
from models import Movie, movies_schema, movie_schema
from setup_db import db

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        try:
            all_movies = db.session.query(Movie).all()
            return movies_schema.dump(all_movies), 200
        except Exception as e:
            return str(e), 404

    def post(self):
        req_json = request.get_json()
        new_movie = Movie(**req_json)
        db.session.add(new_movie)
        db.session.commit()
        db.session.close()

        return "", 201


@movie_ns.route('/d')
class MovieView(Resource):
    def get(self):
        try:
            director_id = request.args['director_id']
            all_movies = Movie.query.filter(Movie.director_id == director_id)
            return movies_schema.dump(all_movies), 200

        except Exception as e:
            return str(e), 404


@movie_ns.route('/g')
class MovieView(Resource):
    def get(self):
        try:
            genre_id = request.args['genre_id']
            all_movies = Movie.query.filter(Movie.genre_id == genre_id)
            return movies_schema.dump(all_movies), 200

        except Exception as e:
            return str(e), 404

@movie_ns.route('/y')
class MovieView(Resource):
    def get(self):
        try:
            year = request.args['year']
            all_movies = Movie.query.filter(Movie.year == year)
            return movies_schema.dump(all_movies), 200

        except Exception as e:
            return str(e), 404


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid: int):
        try:
            movie = db.session.query(Movie.title, Movie.description).filter(Movie.id == bid).one()
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid: int):
        movie = db.session.query(Movie).get(bid)
        req_json = request.get_json()

        movie.title = req_json['title']
        movie.description = req_json['description']
        movie.trailer = req_json['trailer']
        movie.year = req_json['year']
        movie.rating = req_json['rating']
        movie.genre_id = req_json['genre_id']
        movie.director_id = req_json['director_id']

        db.session.add(movie)
        db.session.commit()
        db.session.close()

        return "", 204

    def patch(self, bid: int):
        movie = db.session.query(Movie).get(bid)
        req_json = request.get_json()

        if 'title' in req_json:
            movie.title = req_json['title']
        if 'description' in req_json:
            movie.title = req_json['description']
        if 'trailer' in req_json:
            movie.title = req_json['trailer']
        if 'year' in req_json:
            movie.title = req_json['year']
        if 'rating' in req_json:
            movie.title = req_json['rating']
        if 'genre_id' in req_json:
            movie.title = req_json['genre_id']
        if 'director_id' in req_json:
            movie.title = req_json['director_id']

        db.session.add(movie)
        db.session.commit()
        db.session.close()

        return "", 204

    def delete(self, bid: int):
        movie = db.session.query(Movie).get(bid)

        db.session.delete(movie)
        db.session.commit()
        db.session.close()

        return "", 204
