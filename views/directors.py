from flask_restx import Resource, Namespace
from models import Director, directors_schema, director_schema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        try:
            directors = db.session.query(Director).all()
            return directors_schema.dump(directors), 200
        except Exception as e:
            return str(e), 404


@director_ns.route('/<int:bid>')
class DirectorView(Resource):
    def get(self, bid: int):
        try:
            director = db.session.query(Director).filter(Director.id == bid).one()
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404
