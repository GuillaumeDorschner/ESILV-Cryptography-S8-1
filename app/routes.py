import requests
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from .models import User  # Assurez-vous d'avoir une classe User dans models.py

bp = Blueprint("main", _name_)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@bp.route("/profile")
def profile():
    return render_template("profile.html", email=session["email"])
