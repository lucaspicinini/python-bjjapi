import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG', 'default')
app = create_app(config_name)
app.run()