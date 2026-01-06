from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()  

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7abbca76d02ce6238447e113edaba0efc35683f8ee06cea17e9f1125de6d55095db1417ed13efe1821056c6fe6fd5ce11ffcd84d'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prodiag.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    print(f"Login view is: {login_manager.login_view}")

    migrate.init_app(app, db) 

    from .routes import main
    app.register_blueprint(main)

    return app
