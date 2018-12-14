from flask import Flask
from config import Config 
from flask_moment import Moment
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    

    return app