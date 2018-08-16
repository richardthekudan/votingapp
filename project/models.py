from project import db


class User(db.Model):
    _tablename_ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))
    role = db.Column(db.String(50), default='user')
    voted = db.Column(db.Boolean, default=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Candidate(db.Model):
    _tablename_ = 'candidates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    votes = db.Column(db.Integer, default=0)
