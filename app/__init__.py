from flask import Flask
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy

from .models import User

app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = "dshfkjhqslfdshcuvxciuvuaiujh"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://root:password1234@db/main"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialisation de la base de données
db = SQLAlchemy(app)

# Initialisation de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Import your application's routes
from . import routes
