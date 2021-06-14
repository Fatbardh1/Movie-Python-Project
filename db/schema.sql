DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS directors;
DROP TABLE IF EXISTS movie_actor;
DROP TABLE IF EXISTS movie_director;


CREATE TABLE movies (
    moviesId INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    description TEXT NOT NULL
);


CREATE TABLE actors (
    actorsId INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    nationality TEXT NOT NULL
);


CREATE TABLE directors (
    directorsId INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    nationality TEXT NOT NULL
);

CREATE TABLE movie_actor(
    movies_id INTEGER NOT NULL,
    actors_id INTEGER NOT NULL,
    FOREIGN KEY (actors_id) REFERENCES actors (actorsId),
    FOREIGN KEY (movies_id) REFERENCES movies (moviesId)
);

CREATE TABLE movie_director(
    movies_id INTEGER NOT NULL,
    directors_id INTEGER NOT NULL,
    FOREIGN KEY (directors_id) REFERENCES directors (directorsId),
    FOREIGN KEY (movies_id) REFERENCES movies (moviesId)
);


