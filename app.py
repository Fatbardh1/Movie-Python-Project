import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, Response
from werkzeug.exceptions import abort

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from flask_restful import Api

import controller


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#api = Api(app)
#api.add_resource(MovieListAPI, '/api/movies', endpoint = 'movies')
#api.add_resource(MovieAPI, '/api/movies/<int:moviesId>', endpoint = 'movie')


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


users = [User(id) for id in range(1, 51)]


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "_secret":
            id = username.split("user")[1]
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
<form action="" method="post">
<p><input type=text name=username>
<p><input type=password name=password>
<p><input type=submit value=Login>
</form>
''')


@login_manager.user_loader
def user_loader(user_id):
    return User(user_id)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')





@app.route('/')
def index():
    movies = controller.get_movies()
    return render_template('index.html', movies=movies)





@app.route('/<int:movie_id>')
def movie(movie_id):
    movie = controller.get_movie(movie_id)
    return render_template('movie.html', movie=movie)


@app.route('/create', methods=('GET', 'POST'))
# @login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        description = request.form['description']
        if not title:
            flash('Title is required!')
        else:

            controller.create_movie(title, genre, description)
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:movie_id>/edit', methods=('GET', 'POST'))
def edit(movie_id):
    movie = controller.get_movie(movie_id)
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        description = request.form['description']
        if not title:
            flash('Title is required!')
        else:
            controller.update_movie(movie_id, title, genre, description)
            return redirect(url_for('index'))
    return render_template('edit.html', movie=movie)


@app.route('/<int:movie_id>/delete', methods=('POST',))
def delete(movie_id):
    controller.delete_movie(movie_id)
    flash('Post with id"{}" was successfully deleted!'.format(movie['movie_id']))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
