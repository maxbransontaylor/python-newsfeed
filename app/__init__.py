from os import getenv
from flask import Flask
from app.routes import home, dashboard, api
from app.db import init_db
from app.utils import filters
from dotenv import load_dotenv
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.config.from_mapping(SECRET_KEY=getenv('SESSION_SECRET'))

    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural
    init_db(app)
    return app
