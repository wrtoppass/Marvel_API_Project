from flask import render_template, flash, redirect, url_for, g
from flask_login import current_user, login_required
from . import bp

from app.models import Post, User
from app.forms import PostForm

@bp.route('/post', methods=['GET','POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(body=form.body.data)
        p.user_id = current_user.user_id
        p.commit()
        flash('Published', 'success')
        return redirect(url_for('social.user_page',username=current_user.username))
    return render_template('post.jinja', form = form,user_search_form= g.user_search_form)

@bp.route('/userpage/<username>')
@login_required
def user_page(username):   
    user = User.query.filter_by(username=username).first()
    return render_template('user_page.jinja', title=username, user=user, user_search_form= g.user_search_form)

@bp.post('/user-search')
@login_required
def user_search():
    if g.user_search_form.validate_on_submit:
        return redirect(url_for('social.user_page', username=g.user_search_form.user.data))
    return redirect(url_for('main.home'))