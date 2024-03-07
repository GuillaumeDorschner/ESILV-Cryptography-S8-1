from flask import Flask


def create_app():
    app = Flask(_name_)

    # Initialisation d'autres composants (Base de données, Authentification, etc.)

    from . import routes

    app.register_blueprint(routes.bp)

    return app
