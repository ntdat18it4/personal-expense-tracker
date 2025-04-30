from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import os

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.urandom(24),
        SQLALCHEMY_DATABASE_URI='sqlite:///site.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    csrf.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app