from flask import Flask
from app import routes
from app.create_table import create_table_if_not_exists


create_table_if_not_exists()


def create_app():

    app= Flask(__name__, static_url_path=None)

    routes.init_app(app)

    return app