from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Anime
from . import db
from flask_login import login_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    # login logic
    pass

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    # signup logic
    pass

@main.route('/subscribe', methods=['GET', 'POST'])
@login_required
def subscribe():
    # handle Stripe and update user.subscription
    pass

@main.route('/watch/<int:anime_id>')
@login_required
def watch(anime_id):
    # check user.subscription and access
    pass

@main.route('/search')
def search():
    query = request.args.get('q')
    year = request.args.get('year')
    animes = Anime.query
    if query:
        animes = animes.filter(Anime.name.contains(query))
    if year:
        animes = animes.filter_by(year=year)
    return render_template('search.html', animes=animes.all())
