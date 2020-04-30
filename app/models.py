import datetime

from werkzeug.security import generate_password_hash

from . import db


def _get_date():
    return datetime.datetime.now()


class User(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80), unique=True)
    biography = db.Column(db.String(500))
    profile_photo = db.Column(db.String(80))
    joined_on = db.Column(db.Date, default=_get_date)

    def __init__(self, first_name, last_name, username, password, email, location, biography, profile_photo):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo

    
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' %  self.username




class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer , db.ForeignKey('user_profiles.id'))
    photo = db.Column(db.String(80))
    caption = db.Column(db.String(80))
    created_on = db.Column(db.Date, default=_get_date)

    def __init__(self, user_id, photo, caption):
        self.user_id = user_id
        self.photo = photo
        self.caption = caption



class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer , db.ForeignKey('user_profiles.id'))
    post_id = db.Column(db.Integer , db.ForeignKey('posts.id'))

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id
    
class Follow(db.Model):
    __tablename__ = 'follow'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer , db.ForeignKey('user_profiles.id'))
    follower_id = db.Column(db.Integer , db.ForeignKey('user_profiles.id'))

    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id
    
    