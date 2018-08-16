from flask import Blueprint, render_template, request, redirect, session, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from project import db, login_manager
from project.models import User, Candidate
from sqlalchemy import asc

routes = Blueprint('routes', __name__, template_folder='templates')


@routes.route('/')
def home():
    return redirect(url_for('routes.login'))


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                session['user'] = username
                login_user(user)
                return redirect(url_for('routes.user_dashboard'))
        return render_template('login.html', login_failed=True)
    else:
        return render_template('login.html')


@routes.route('/user_dashboard', methods=['GET', 'POST'])
@login_required
def user_dashboard():
    user = User.query.filter_by(username=session['user']).first()
    candidates = Candidate.query.order_by(asc(Candidate.name)).all()
    if user.role == 'user':
        return render_template('finished.html', voted=True) if user.voted else render_template('user.html', user=user,
                                                                                               candidates=candidates)
    elif user.role == 'admin':
        return render_template('admin.html', candidates=candidates)


@routes.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('routes.login'))


@routes.route('/vote', methods=['GET', 'POST'])
@login_required
def vote():
    candidate_name = request.form['options']
    username = session['user']
    candidate = Candidate.query.filter_by(name=candidate_name).first()
    candidate.votes += 1
    user = User.query.filter_by(username=username).first()
    user.voted = True
    db.session.add(user)
    db.session.add(candidate)
    db.session.commit()
    return render_template('finished.html', finished=True)


@login_manager.unauthorized_handler
def handle_needs_login():
    return redirect(url_for('routes.login'))
