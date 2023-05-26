from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.models import User
from flask_login import current_user

from . import bp
from app.forms import RegisterForm, SigninForm

@bp.route('/signin', methods=['GET',"POST"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash(f'{form.username.data} signed in','success')
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash(f'{form.username.data} doesn\'t exist or incorrect password','warning')
    return render_template('signin.jinja', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=form.username.data,email=form.email.data)
            u.password = u.hash_password(form.password.data)
            u.add_token()
            u.commit()
            flash(f"{form.username.data} registered", 'success')
            return redirect(url_for("main.home"))
        if user:
            flash(f'{form.username.data} already taken, try again','warning')
        else:
            flash(f'{form.email.data} already taken, try again','warning')
    return render_template('register.jinja', form=form)