from app import create_app, db
from app.models import User

def init_db():
    app = create_app()
    with app.app_context():
        # Create database tables
        db.create_all()
        
        # Check if admin user exists
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', email='admin@example.com', role='admin')
            admin.set_password('admin123')  # Change this in production!
            db.session.add(admin)
            db.session.commit()
            print('Admin user created!')
        else:
            print('Admin user already exists.')

if __name__ == '__main__':
    init_db() 