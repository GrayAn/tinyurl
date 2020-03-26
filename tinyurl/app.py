from flask import Flask

from config import get_config
from database import db
from views import views_blueprint


class Application:
    def __init__(self):
        cfg = get_config()

        self.app = Flask(__name__)
        self.app.register_blueprint(views_blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = cfg.db_url
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['TINYURL_URLLENGTH'] = cfg.url_length
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
