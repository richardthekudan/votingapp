from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from settings import settings


app = Flask(__name__)
app.config['SECRET_KEY'] = settings['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = settings['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

from project.routes import routes

app.register_blueprint(routes)


from project.models import User

login_manager.login_view = "/login"


@login_manager.user_loader
def load_user(user):
    return User.query.get(user)
