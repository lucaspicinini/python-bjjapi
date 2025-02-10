import os
from app import create_app

config_name = os.getenv('API_CONFIG', 'default')
app = create_app(config_name)