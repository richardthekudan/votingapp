from project import db
from project.models import User, Candidate
from werkzeug.security import generate_password_hash

db.drop_all()
db.create_all()

admin = User(username='admin', password=generate_password_hash('admin'), role='admin')
db.session.add(admin)

for i in range(1, 51):
    username = 'user' + str(i)
    password = 'pwd' + str(i)
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    if i < 6:
        candidate = Candidate(name='candidate'+str(i))
        db.session.add(candidate)

db.session.commit()
