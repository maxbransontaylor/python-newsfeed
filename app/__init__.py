from flask import Flask
from app.routes import home, dashboard
from app.db import init_db


def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.config.from_mapping(SECRET_KEY='super_secret_key')

    @app.route('/hello')
    def hello():
        return 'hello world'

    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    init_db()
    return app
