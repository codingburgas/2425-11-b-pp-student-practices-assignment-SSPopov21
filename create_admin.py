from app import db
from app.models.user import User

admin = User(
    username='admin',
    email='admin@admin.com',
    role='admin',
    is_admin=True
)
admin.set_password('12345678')
db.session.add(admin)
db.session.commit()
print("Admin user created!") 