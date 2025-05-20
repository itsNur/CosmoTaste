from dotenv import load_dotenv
load_dotenv()  # Call it right away to load variables from .env

from flask import Flask
from .routes import bp


app = Flask(__name__)

# Blueprints registrations
app.register_blueprint(bp)

# Any other app configuration that might need env vars
# app.config['SOME_SETTING'] = os.getenv('SOME_ENV_VAR')
