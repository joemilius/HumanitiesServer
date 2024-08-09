#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Membership, Group, Invitation, Activity, Music, Movie, Book, Music_Comment, Movie_Comment, Book_Comment

# Views go here!

@app.route('/')
def index():
    return '<h1>Humanities Server</h1>'

class SignUp(Resource):
    def post(self):
        json = request.get_json()
        user = User(
            username = json.get('username'),
            email = json.get('email'),
            first_name = json.get('first_name'),
            last_name = json.get('last_name'),
            logins = 1
        )

        user.passowrd_hash = json.get('password')

        try:
            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id

            return user.to_dict(), 201
        except IntegrityError:
            return {'error': '422 Unprocessable Entity'}, 422
        

class CheckSession(Resource):


    def get(self):
        
        user_id = session['user_id']
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            return user.to_dict(), 200
        
        return {}, 401

class Login(Resource):
    
    def post(self):

        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')

        user = User.query.filter(User.username == username).first()
        
        if user:
            if user.authenticate(password):

                session['user_id'] = user.id
                return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401
    
class Logout(Resource):

    def delete(self):

        session['user_id'] = None
        
        return {}, 204
    
class AllGroups(Resource):

    def get(self):
        groups = [group.to_dict() for group in Group.query.all()]

        return make_response(groups, 200)
    
class OneGroup(Resource):

    def get(self, id):
        group = Group.query.filter_by(id=id).first()

        return make_response(group.to_dict(), 200)
    
class OneMembership(Resource):

    def get(self, id):
        membership = Membership.query.filter_by(id=id).first()

        return make_response(membership.to_dict(), 200)
    
class OneInvitation(Resource):

    def get(self, id):
        invitation = Invitation.query.filter_by(id=id).first()

        return make_response(invitation.to_dict(), 200)
    
class OneMovie(Resource):

    def get(self, id):
        movie = Movie.query.filter_by(id=id).first()

        return make_response(movie.to_dict(), 200)
    
class AllMovies(Resource):

    def get(self):
        movies = [movie.to_dict() for movie in Movie.query.all()]

        return make_response(movies, 200)
    
class OneMusic(Resource):

    def get(self, id):
        music = Music.query.filter_by(id=id).first()

        return make_response(music.to_dict(), 200)
    
class OneBook(Resource):

    def get(self, id):
        book = Book.query.filter_by(id=id).first()

        return make_response(book.to_dict(), 200)
    
class OneMovieComment(Resource):

    def get(self, id):
        movie_comment = Movie_Comment.query.filter_by(id=id).first()

        return make_response(movie_comment.to_dict(), 200)
    
class OneMusicComment(Resource):

    def get(self, id):
        music_comment = Music_Comment.query.filter_by(id=id).first()

        return make_response(music_comment.to_dict(), 200)
    
class OneBookComment(Resource):

    def get(self, id):
        book_comment = Book_Comment.query.filter_by(id=id).first()

        return make_response(book_comment.to_dict(), 200)



api.add_resource(SignUp,"/signup")
api.add_resource(Login, "/login")
api.add_resource(CheckSession, "/check-session")
api.add_resource(Logout, "/logout")
api.add_resource(AllGroups, "/groups")
api.add_resource(OneGroup, "/groups/<int:id>")
api.add_resource(OneMembership, "/memberships/<int:id>")
api.add_resource(OneInvitation, "/invitations/<int:id>")
api.add_resource(OneMovie, "/movies/<int:id>")
api.add_resource(AllMovies, "/movies")
api.add_resource(OneMusic, "/music/<int:id>")
api.add_resource(OneBook, "/books/<int:id>")
api.add_resource(OneMovieComment, "/moviecomments/<int:id>")
api.add_resource(OneMusicComment, "/musiccomments/<int:id>")
api.add_resource(OneBookComment, "/bookcomments/<int:id>")


if __name__ == '__main__':
    app.run(port=5555, debug=True)