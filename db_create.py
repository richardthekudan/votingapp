from model import db, Users, Candidates
from werkzeug.security import generate_password_hash

db.create_all()

admin = Users('admin', generate_password_hash('admin'), 'admin', False)

user1 = Users('user1', generate_password_hash('pwd1'))
user2 = Users('user2', generate_password_hash('pwd2'))
user3 = Users('user3', generate_password_hash('pwd3'))
user4 = Users('user4', generate_password_hash('pwd4'))
user5 = Users('user5', generate_password_hash('pwd5'))

candidate1 = Candidates('candidate1')
candidate2 = Candidates('candidate2')
candidate3 = Candidates('candidate3')
candidate4 = Candidates('candidate4')
candidate5 = Candidates('candidate5')
candidate6 = Candidates('candidate6')

db.session.add(admin)
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.add(user5)
db.session.add(candidate1)
db.session.add(candidate2)
db.session.add(candidate3)
db.session.add(candidate4)
db.session.add(candidate5)
db.session.add(candidate6)

db.session.commit()
