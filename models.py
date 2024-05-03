from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from server import bcrypt

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    first_name = db.column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    logins = db.Column(db.Integer)
    _password_hash = db.Column(db.String, nullable=False)

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
class Membership(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    user = db.relationship('User', back_populates='memberships')
    group = db.relationship('Group', back_populates='memberships')