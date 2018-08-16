from flask import Flask, flash, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash

from model import db, Users, Candidates


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thekkudr:qwerty@localhost:5432/votingapp'

db.init_app(app)


@app.route('/')
def home():
    return redirect(url_for('vote'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(username=username).first()
        candidates = Candidates.query.all()

        if user:
            if check_password_hash(user.password, password):
                session['user'] = username
                flash('Login was successfull')
            if user.role == 'user':
                return render_template('user.html', candidates=candidates)
            else:
                return render_template('admin.html', candidates=candidates)
        else:
            flash('Username or password is incorrect please try again', 'error')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')

        flash('We hope to see you again!')

    return redirect(url_for('login'))


@app.route('/vote', methods=['POST', 'GET'])
def vote():
    render_template()


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
