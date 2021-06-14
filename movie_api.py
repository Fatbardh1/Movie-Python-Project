from flask_restful import Api, Resource
from flask_restful import reqparse
from flask_restful import fields, marshal
import controller

movie_fields = {
    'moviesId': fields.Integer,
    'title': fields.String,
    'genre': fields.String,
    'description': fields.String
}

class MovieListAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                               help='No post title provided', location='json')
        self.reqparse.add_argument('genre', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        super(MovieListAPI, self).__init__()

    def get(self):
        movies = controller.get_movies()
        return {'posts': marshal(movies, movie_fields)}

    def movie(self):
        args = self.reqparse.parse_args()
        controller.create_movie(args['title'], args['genre'], args['description'])
        return {'message': 'success'}


class MovieAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('genre', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        super(MovieAPI, self).__init__()

    def get(self, movieId):
        post = controller.get_movie(movieId)
        return {'movie': marshal(post, movie_fields)}

    def put(self, moviesId):
        args = self.reqparse.parse_args()
        controller.update_movie(moviesId, args['title'], args['genre'], args['description'])
        return {'message': 'success'}

    def delete(self, moviesId):
        controller.delete_movie(moviesId)
        return {'message': 'success'}



