from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

db = SQLAlchemy()
# migrate = Migrate()

def create_app():
    app = Flask(__name__)
    from . import DBconfig

    app.config.from_object(DBconfig)

    db.init_app(app)
    # migrate.init_app(app,db)
    with app.app_context():
        from api import register_routes

        register_routes(app)

        db.create_all()

    return app
