from app import db


class Movies(db.Model):
    __tablename__ = "movies"
    moviesId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Movies %r>' % self.title

class Actors(db.Model):
    __tablename__ = "actors"
    actorsId = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=False)
    nationality = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Movies %r>' % self.firstname


class Directors(db.Model):
    __tablename__ = "directors"
    directorsId = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=False)
    nationality = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Movies %r>' % self.firstname
