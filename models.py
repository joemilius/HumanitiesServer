from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = (
        '-memberships.user',
        '-invitations.user',
        '-groups.users',
        '-groups.invitations'
        '-movies.users',
        '-music.users',
        '-books.users',
        '-movies.group',
        '-music.group',
        '-books.group',
        '-movies.movie_comments.user',
        '-music.music_comments.user',
        '-books.book_comments.user',
        '-movie_comments.user',
        '-music_comments.user',
        '-book_comments.user',
        '-movie_comments.movie.users',
        '-music_comments.music.users',
        '-book_comments.book.users',
        '-movie_comments.movie.group',
        '-music_comments.music.group',
        '-book_comments.book.group',
        '-movie_comments.movie.movie_comments',
        '-music_comments.music.music_comments',
        '-book_comments.book.book_comments',
        '-my_movies.user',
        '-my_music.user',
        '-my_books.user'
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    logins = db.Column(db.Integer)
    _password_hash = db.Column(db.String, nullable=False)

    memberships = db.relationship(
        'Membership', back_populates='user', cascade='all, delete-orphan')
    
    invitations = db.relationship(
        'Invitation', back_populates='user', cascade='all, delete-orphan')
    
    groups = association_proxy('memberships', 'group',
                                 creator=lambda project_obj: Membership(project=project_obj))
    
    # new_invites = association_proxy('invitations', 'group',
    #                              creator=lambda project_obj: Invitation(project=project_obj))
    
    movies = association_proxy('movie_comments', 'movie',
                                 creator=lambda project_obj: Movie_Comment(project=project_obj))
    movie_comments = db.relationship(
        'Movie_Comment', back_populates='user', cascade='all, delete-orphan')
    
    music = association_proxy('music_comments', 'music',
                                 creator=lambda project_obj: Movie_Comment(project=project_obj))
    music_comments = db.relationship(
        'Music_Comment', back_populates='user', cascade='all, delete-orphan')
    
    books = association_proxy('book_comments', 'book',
                                 creator=lambda project_obj: Movie_Comment(project=project_obj))
    book_comments = db.relationship(
        'Book_Comment', back_populates='user', cascade='all, delete-orphan')
    
    my_movies = db.relationship(
        'My_Movie', back_populates='user', cascade='all, delete-orphan')
    
    my_music = db.relationship(
        'My_Music', back_populates='user', cascade='all, delete-orphan')
    
    my_books = db.relationship(
        'My_Book', back_populates='user', cascade='all, delete-orphan')

    @hybrid_property
    def password(self):
        # raise Exception('Password hashes may not be viewed')
        return None
    
    @password.setter
    def password(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    


class Group(db.Model, SerializerMixin):
    __tablename__ = 'groups'

    serialize_rules = (
        '-memberships.group',
        '-memberships.user.memberships',
        '-memberships.user.invitations',
        '-memberships.user.movie_comments',
        '-memberships.user.music_comments',
        '-memberships.user.book_comments',
        '-users.groups',
        '-users.memberships',
        '-users.invitations',
        '-users.movie_comments',
        '-users.music_comments',
        '-users.book_comments',
        '-invitations.group',
        '-invitations.user.invitations',
        '-invitations.user.memberships',
        '-invitations.user.movie_comments',
        '-invitations.user.music_comments',
        '-invitations.user.book_comments',
        '-activities.group',
        '-movies.group',
        '-music.group',
        '-books.group',
        '-movies.movie_comments.user',
        '-music.music_comments.user',
        '-books.book_comments.user',
    )

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String, nullable=False)

    memberships = db.relationship(
        'Membership', back_populates='group', cascade='all, delete-orphan')
    
    users = association_proxy('memberships', 'user',
                                 creator=lambda project_obj: Membership(project=project_obj))
    
    invitations = db.relationship(
        'Invitation', back_populates='group', cascade='all, delete-orphan')
    
    activities = db.relationship(
        'Activity', back_populates='group', cascade='all, delete-orphan')
    
    movies = db.relationship(
        'Movie', back_populates='group', cascade='all, delete-orphan')
    
    music = db.relationship(
        'Music', back_populates='group', cascade='all, delete-orphan')
    
    books = db.relationship(
        'Book', back_populates='group', cascade='all, delete-orphan')
    
    
    
class Membership(db.Model, SerializerMixin):
    __tablename__ = 'memberships'

    serialize_rules = ('-user.memberships', '-group.memberships')

    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    user = db.relationship('User', back_populates='memberships')
    group = db.relationship('Group', back_populates='memberships')

class Invitation(db.Model, SerializerMixin):
    __tablename__ = 'invitations'

    serialize_rules = ('-user.invitations', '-group.invitations',)

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    accepted = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    user = db.relationship('User', back_populates='invitations')
    group = db.relationship('Group', back_populates='invitations')


class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'

    serialize_rules = ('-group.activities')

    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String)
    description = db.Column(db.String)
    votes = db.Column(db.Integer)
    date = db.Column(db.Date)
    time = db.Column(db.Time)

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    group = db.relationship('Group', back_populates='activities')


class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    serialize_rules = ('-group.movies', '-movie_comments.movie', '-users.movies',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    year = db.Column(db.Integer)
    director = db.Column(db.String)
    cast = db.Column(db.String)
    description = db.Column(db.String)

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    group = db.relationship('Group', back_populates='movies')

    movie_comments = db.relationship(
        'Movie_Comment', back_populates='movie', cascade='all, delete-orphan')
    
    users = association_proxy('movies', 'user',
                                 creator=lambda project_obj: Movie_Comment(project=project_obj))


class Music(db.Model, SerializerMixin):
    __tablename__ = 'musics'

    serialize_rules = ('-group.music', '-music_comments.music', '-users.music')

    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String)
    album_name = db.Column(db.String)
    image = db.Column(db.String)
    year = db.Column(db.Integer)
    description = db.Column(db.String)

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    group = db.relationship('Group', back_populates='music')

    music_comments = db.relationship(
        'Music_Comment', back_populates='music', cascade='all, delete-orphan')
    
    songs = db.relationship(
        'Song', back_populates='album', cascade='all, delete-orphan')
    
    users = association_proxy('music_comments', 'user',
                                 creator=lambda project_obj: Movie_Comment(project=project_obj))



class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    serialize_rules = ('-group.books', '-book_comments.book', '-users.books',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)
    
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    group = db.relationship('Group', back_populates='books')

    book_comments = db.relationship(
        'Book_Comment', back_populates='book', cascade='all, delete-orphan')
    
    users = association_proxy('books_commnets', 'user',
                                 creator=lambda project_obj: Movie_Comment(project=project_obj))


class Movie_Comment(db.Model, SerializerMixin):
    __tablename__ = 'movie_comments'

    serialize_rules = ('-movies.movie_comments', '-user.movie_comment',)

    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)
    content = db.Column(db.String)

    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

    movie = db.relationship('Movie', back_populates='movie_comments')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='movie_comments')


class Music_Comment(db.Model, SerializerMixin):
    __tablename__ = 'music_comments'

    serialize_rules = ('-music.music_comments', '-user.music_comments',)

    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)
    content = db.Column(db.String)

    music_id = db.Column(db.Integer, db.ForeignKey('musics.id'))

    music = db.relationship('Music', back_populates='music_comments')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='music_comments')


class Book_Comment(db.Model, SerializerMixin):
    __tablename__ = 'book_comments'

    serialize_rules = ('-book.book_comments', '-user.book_comments',)

    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)
    content = db.Column(db.String)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    book = db.relationship('Book', back_populates='book_comments')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='book_comments')

class My_Movie(db.Model, SerializerMixin):
    __tablename__ = 'my_movies'

    serialize_rules= ('user.my_movies',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    year = db.Column(db.Integer)
    director = db.Column(db.String)
    cast = db.Column(db.String)
    description = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='my_movies')

class My_Music(db.Model, SerializerMixin):
    __tablename__ = 'my_music'

    serialize_rules= ('user.my_music',)

    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String)
    album_name = db.Column(db.String)
    image = db.Column(db.String)
    year = db.Column(db.Integer)
    description = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='my_music')

class My_Book(db.Model, SerializerMixin):
    __tablename__ = 'my_books'

    serialize_rules= ('user.my_books',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='my_books')

class Song(db.Model, SerializerMixin):
    __tablename__ = 'songs'

    serialize_rules = ('-album.songs',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    run_time = db.Column(db.String)

    music_id = db.Column(db.Integer, db.ForeignKey('musics.id'))

    album = db.relationship('Music', back_populates='songs')