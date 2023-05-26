from flask import render_template, g

from . import bp 
from app import app
from app.forms import UserSearchForm

@app.before_request
def before_request():
    g.user_search_form = UserSearchForm()

@bp.route('/')
def home():
    matrix = {
        'instructors': ('Sean', "Dylan"),
        'students': ['ray', 'hamed', 'gian', 'ben', 'christopher', 'alec']
    }
    return render_template('index.jinja', title='Home', instructors=matrix['instructors'], students=matrix['students'],user_search_form= g.user_search_form)

@bp.route('/about')
def about():
    return render_template('about.jinja',user_search_form= g.user_search_form)