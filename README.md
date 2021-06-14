# Movie-Python-Project

Flask is an API of Python that allows us to build up web-applications.

# Installation

pip install -r requirements.txt
```
or
You just type the requirement libraries such as 

flask==2.0.1
flask_sqlalchemy
flask-login
flask_restful

and you download them automatically.

# Usage
from flask import Flask, render_template, request, url_for, flash, redirect, Response

return render_template('index.html') #returns the index template
return render_template('create.html') #returns template to create new movie

# Parts of the code

def get_movies(): #this method finds all movies
    return Movies.query.all()
movies = controller.get_movies()  #and displays them
    return render_template('index.html', movies=movies)
  
  
def create_movie(title, genre, description): #method for creating a movie
@app.route('/create', methods=('GET', 'POST')) # the route for creating a movie


def update_movie(movie_id, title, genre, description): #updating a movie
@app.route('/<int:movie_id>/edit', methods=('GET', 'POST'))  #route to edit 



def delete_movie(movie_id):#deleting a movie
  flash('Post with id"{}" was successfully deleted!'.format(movie['movie_id']))
    return redirect(url_for('index'))   #displaying that movie was successfully deleted
    

# Contributing
Feel free to contribute! xoxo
