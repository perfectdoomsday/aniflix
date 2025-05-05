from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    subscription = db.Column(db.String(50))  # 'free', 'basic', 'premium'

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.Text)
    year = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    video_url = db.Column(db.String(200))
