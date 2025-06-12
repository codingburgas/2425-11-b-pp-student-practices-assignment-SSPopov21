from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from config import Config
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
mail = Mail()
bootstrap = Bootstrap()
csrf = CSRFProtect()

@login_manager.user_loader
def load_user(id):
    from app.models.user import User
    return User.query.get(int(id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'job_success.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    # Import models to ensure they are registered with SQLAlchemy
    from app.models.user import User
    from app.models.survey import Survey
    from app.models.job_offer import JobOffer

    # Register blueprints
    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.routes.survey import bp as survey_bp
    app.register_blueprint(survey_bp, url_prefix='/survey')

    from app.routes.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from app.routes.job_offers import bp as job_offers_bp
    app.register_blueprint(job_offers_bp, url_prefix='/job-offers')

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
