#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
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

if __name__ == '__main__':
    app.run(port=5555, debug=True)