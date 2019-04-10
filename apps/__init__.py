from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from apps.book.views import web as bookweb
    from apps.user.views import web as userweb

    app.register_blueprint(blueprint=bookweb)
    app.register_blueprint(blueprint=userweb)
