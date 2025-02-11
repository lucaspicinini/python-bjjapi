import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_ENGINE_OPTIONS={'pool_pre_ping': True}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER={
        "info": {
            "title": "BJJ API Docs",
            "description":
                "BJJ API is the world's only public database in Portuguese dedicated to Brazilian Jiu-Jitsu, "
                "providing detailed information on the greatest BJJ fighters in history."
                "\n\n"
                "Built for enthusiasts, researchers and developers, "
                "this open-source API delivers comprehensive data in Portuguese, "
                "making BJJ knowledge more accessible than ever.",
            "contact": {
                "url": "https://github.com/lucaspicinini",
            },
            "termsOfService": "https://github.com/lucaspicinini/python-bjjapi",
            "version": "0.0.1"
        },
        "externalDocs": {
            "description": "BJJ API Docs",
            "url": "https://github.com/lucaspicinini/python-bjjapi",
        },
        "specs_route": "/docs/",
        "schemes": ["http"],
        "specs": [{"endpoint": "specs", "route": "/specs_v1"}],

    }

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False

class TestConfig(Config):
    TESTING = True

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
    'default': DevConfig
}

