from flask import Blueprint, render_template, redirect, url_for, request, session
from .models import User  # Assurez-vous d'avoir une classe User dans models.py
import requests

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


@bp.route('/profile')
def profile():
    return render_template('profile.html', email=session['email'])

