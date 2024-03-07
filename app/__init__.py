from flask import Flask

def create_app():
    app = Flask(__name__)

    # Initialisation d'autres composants (Base de données, Authentification, etc.)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
