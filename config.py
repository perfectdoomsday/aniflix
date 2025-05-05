import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'anime-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///animeflix.db'
    STRIPE_PUBLIC_KEY = 'your_public_key'
    STRIPE_SECRET_KEY = 'your_secret_key'
