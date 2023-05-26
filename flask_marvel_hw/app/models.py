from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from secrets import token_urlsafe

from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    token = db.Column(db.String(250), unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def add_token(self):
        setattr(self,'token',token_urlsafe(32))
    
    def get_id(self):
        return str(self.user_id)
    
class Post(db.Model):
    id=  db.Column(db.Integer, primary_key = True)
    body= db.Column(db.String(250))
    timestamp= db.Column(db.DateTime, default=datetime.utcnow)
    user_id= db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):
        return f'<Post: {self.body}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()