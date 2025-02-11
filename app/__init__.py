from flask import Flask
from flasgger import Swagger

from app.config import config
from app.home.controller import home_bp
from app.fighters.controller import fighters_bp
from app.teams.controller import teams_bp
from app.lineages.controller import lineages_bp
from app.achievements.controller import achievements_bp
from app.db import db

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    # app mode
    app.config.from_object(config[config_name])

    # init API Swagger
    swagger = Swagger(app)

    #routes
    app.register_blueprint(home_bp)
    app.register_blueprint(fighters_bp)
    app.register_blueprint(teams_bp)
    app.register_blueprint(lineages_bp)
    app.register_blueprint(achievements_bp)

    # database connection
    db.init_app(app)

    return app