from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    from . import DBconfig

    app.config.from_object(DBconfig)

    db.init_app(app)
    with app.app_context():
        from api import register_routes

        register_routes(app)

        db.create_all()

    return app
