'''Main Application for Twitoff'''
from flask import Flask
from .models import DB




def create_app():
    """Create and configures an instance of the Flask application"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitoff_db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return "Welcome to our app!"
    return app
