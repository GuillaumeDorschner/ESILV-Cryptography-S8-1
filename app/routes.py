from flask import flash, redirect, render_template, request, url_for

from . import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # if user auth
    # if user is not auth
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # if user auth
    # if user is not auth
    return render_template("login.html")


@app.route("/logout")
def logout():
    # logout user

    # redirect to index
    return redirect(url_for("/"))
