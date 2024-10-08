from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    from . import DBconfig_private

    app.config.from_object(DBconfig_private)

    db.init_app(app)
    migrate = Migrate(app, db)
    with app.app_context():
        from api import register_routes

        register_routes(app)

        db.create_all()

    return app
