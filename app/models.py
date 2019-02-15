from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    name = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    the_pitchie = db.relationship('Pitchies', backref='user', lazy='dynamic')

    # comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
         raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'{self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    # users = db.relationship('User',backref = 'role',lazy="dynamic")


class Pitchies(db.Model):
    pitchie_list=[]
    __tablename__ = 'pitchies'

    id = db.Column(db.Integer,primary_key = True)
    post = db.Column(db.String(255), index = True)
    title = db.Column(db.String(255),index = True)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    comments = db.ForeignKey('Comment',  lazy = 'dynamic')

    def __init__(self,title,post,user):
        self.user = user
        self.title = title
        self.post = post

    def save_pitchies(self):
        '''
        Function that saves all pitchies posted
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_pitchies(cls):
        '''
        Function that queries database and returns all posted pitchies.
        '''
        pitches = Pitchies.query.all()
        return pitches

    @classmethod
    def delete_all_pitchies(cls):
        Pitchies.all_pitchies.delete()

class Category(db.Model):
    '''
    Function that will define all the different categories of pitchies.
    '''
    __tablename__ ='categories'


    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255))
    category_description = db.Column(db.String(255))

    @classmethod
    def get_categories(cls):
        '''
        Function that queries the database and returns all the categories from the database
        '''
        categories = Category.query.all()
        return categories


class Comment(db.Model):
    comments_list=[]
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),index = True)
    pitchie_id = db.Column(db.Integer,db.ForeignKey('pitchies.id'))
    commenter_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment_itself=db.Column(db.String(255),index = True)
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,name,comment_itself,pitchie):
        self.name = name
        self.comment_itself = comment_itself
        self.pitchie = pitchie

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitchie_comments(cls,pitchie_id):
        comments = Comment.query.filter_by(pitchie_id=pitchie_id).all()

        return comments

    @classmethod
    def delete_all_pitchies(cls):
        Pitchies.all_pitchies.delete()


class Subscribe(db.Model):
    __tablename__='subscribe'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    email=db.Column(db.String(255),unique = True,index = True, nullable=False)

    def __repr__(self):
        return f'{self.email}'
