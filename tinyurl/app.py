import os

from flask import Flask
from yaml import load, SafeLoader

from database import db
from views import views_blueprint


class Application:
    def __init__(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        config_file_path = os.path.normpath(os.path.join(current_directory, '..', 'config.yml'))
        with open(config_file_path, 'r') as f:
            config_data = load(f.read(), SafeLoader)

        self.app = Flask(__name__)
        self.app.register_blueprint(views_blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = config_data['DBURL']
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['TINYURL_URLLENGTH'] = config_data['URLLength']
        db.init_app(self.app)
        # TODO: Migration script for creating database tables

    def run(self, host=None, port=None, debug=None):
        self.app.run(host, port, debug)

    def wsgi_app(self, environ, start_response):
        return self.app.wsgi_app(environ, start_response)

    def __call__(self, environ, start_response):
        return self.app.__call__(environ, start_response)


if __name__ == '__main__':
    application = Application()
    application.run()
