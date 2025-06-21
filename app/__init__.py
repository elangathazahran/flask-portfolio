import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    from app import routes, models
    from app.routes import main

    app.register_blueprint(main)

    return app
