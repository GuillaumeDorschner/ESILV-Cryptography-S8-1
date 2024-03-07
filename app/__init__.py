from flask import Flask

app = Flask(__name__)

# todo: add database
# todo: add AuthManager

from . import routes
