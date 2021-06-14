from model import Movies
from model import Actors
from app import db


def get_movies():
    return Movies.query.all()


def get_actors():
    return Actors.query.all()


def get_movie(movie_id):
    return Movies.query.filter_by(moviesId=movie_id).first()


def create_movie(title, genre, description):
    movie = Movies(title=title, genre=genre, description=description)
    db.session.add(movie)
    db.session.commit()


def update_movie(movie_id, title, genre, description):
    movie = get_movie(movie_id)
    movie.title = title
    movie.genre = genre
    movie.description = description
    db.session.commit()


def delete_movie(movie_id):
    movie = get_movie(movie_id)
    db.session.delete(movie)
    db.session.commit()
