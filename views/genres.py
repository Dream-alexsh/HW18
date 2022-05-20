from flask_restx import Resource, Namespace
from models import Genre, genres_schema
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        try:
            genres = db.session.query(Genre).all()
            return genres_schema.dump(genres), 200
        except Exception as e:
            str(e), 404


@genre_ns.route('/<int:bid>')
class GenreView(Resource):
    def get(self, bid: int):
        try:
            genre = db.session.query(Genre).filter(Genre.id == bid).all()
            return genres_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404
