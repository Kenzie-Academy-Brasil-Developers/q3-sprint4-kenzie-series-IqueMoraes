from flask import Flask
from app.routes.routes_series import bp_series



def init_app(app: Flask) -> None:

    app.register_blueprint(bp_series)
