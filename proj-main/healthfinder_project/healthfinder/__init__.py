import os
from flask import Flask
from healthfinder.db import db

def create_app():
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../healthfinder.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Import and register blueprints
    from healthfinder.routes.hospitals import hospitals_bp
    from healthfinder.routes.main import main_bp
    from healthfinder.routes.users import users_bp
    from healthfinder.routes.users import admin_bp
    from healthfinder.routes.medicines import medicines_bp
    
    app.register_blueprint(hospitals_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(medicines_bp)
    return app

