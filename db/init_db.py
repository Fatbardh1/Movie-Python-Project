import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO movies (title, genre, description) VALUES (?, ?, ?)",
            ('Bird Box', 'Drama', 'Based on Josh Malerman book of the same name'))
cur.execute("INSERT INTO movies (title, genre, description) VALUES (?, ?, ?)",
            ('Extraction', 'Action', 'A guy sneaks out of his house to visit a club, where he is kidnapped by police '
                                     'officers working for rival drug lord'))
cur.execute("INSERT INTO movies (title, genre, description) VALUES (?, ?, ?)",
            ('Money Heist', 'Action, Drama', 'Eight thieves take hostages and lock themselves in the Royal Mint of '
                                             'Spain as a criminal'))

cur.execute("INSERT INTO actors (firstname, lastname, nationality) VALUES (?, ?, ?)",
            ('Sandra', 'Bulok', 'American'))
cur.execute("INSERT INTO actors (firstname, lastname, nationality) VALUES (?, ?, ?)",
            ('Chris', 'Hemsworth', 'Australian'))
cur.execute("INSERT INTO actors (firstname, lastname, nationality) VALUES (?, ?, ?)",
            ('Ursula', 'Corbero', 'Spanish'))


cur.execute("INSERT INTO directors (firstname, lastname, nationality) VALUES (?, ?, ?)",
            ('Susanne', 'Bier', 'Danish'))
cur.execute("INSERT INTO directors (firstname, lastname, nationality) VALUES (?, ?, ?)",
            ('Sam', 'Hargrave', 'American'))
cur.execute("INSERT INTO directors (firstname, lastname, nationality) VALUES (?, ?, ?)",
            ('Alex', 'Pina', 'Spanish'))

cur.execute("INSERT INTO movie_actor(movies_Id, actors_Id) VALUES(?, ?)", ('1', '1'))
cur.execute("INSERT INTO movie_actor(movies_Id, actors_Id) VALUES(?, ?)", ('2', '2'))
cur.execute("INSERT INTO movie_actor(movies_Id, actors_Id) VALUES(?, ?)", ('3', '3'))

cur.execute("INSERT INTO movie_director(movies_Id, directors_Id) VALUES(?, ?)", ('1', '1'))
cur.execute("INSERT INTO movie_director(movies_Id, directors_Id) VALUES(?, ?)", ('2', '2'))
cur.execute("INSERT INTO movie_director(movies_Id, directors_Id) VALUES(?, ?)", ('3', '3'))

connection.commit()
connection.close()
