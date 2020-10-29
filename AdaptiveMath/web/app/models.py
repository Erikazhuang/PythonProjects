from app import db #from app package in __init__ db = SQLAlchemy(app)
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(1000),index=True, unique= True)
    categoryid = db.Column(db.Integer,db.ForeignKey('category.id'),)

    questions = db.relationship('Question',backref='skill',lazy='dynamic')

    def asdict(self):
        return {'id':self.id,'skill':self.skill}

    def __iter__(self):
        yield 'id', self.id
        yield 'skill', self.skill

    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k,v)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(1000),index=True, unique= True)

    skills = db.relationship('Skill', backref='category', lazy = 'dynamic')

    def asdict(self):
        return {'id':self.id,'category':self.category}

    def __iter__(self):
        yield 'id', self.id
        yield 'category', self.category

    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k,v)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    level = db.Column(db.Integer,default =0)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    records = db.relationship('Record',backref='user',lazy='dynamic')

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Question(db.Model):
    qid = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000),index=True, unique= True)
    answer = db.Column(db.String(1000),index=True)
    explain = db.Column(db.String(1000))
    level = db.Column(db.Integer)
    questiontype =  db.Column(db.String(1000),index=True)
    datecreated = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    active = db.Column(db.Boolean, default = True)
    skillid = db.Column(db.Integer,db.ForeignKey('skill.id'))

    records = db.relationship('Record',backref='question',lazy='dynamic')
  
    def __init__(self,dictionary):
        for k,v in dictionary.items():
            setattr(self,k,v)
    
    def __repr__(self):
        return '<Question {}>'.format(self.question)

    def asdict(self):
        return {'qid':self.qid,'question':self.question,'answer':self.answer,'explain':self.explain}

    def __iter__(self):
        yield 'qid', self.qid
        yield 'question', self.question
        yield 'answer', self.answer
        yield 'explain', self.explain

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer,db.ForeignKey('user.id'),index=True)
    testid = db.Column(db.Integer,index=True)
    questionid = db.Column(db.Integer,db.ForeignKey('question.qid'),index=True)
    response = db.Column(db.String(1000))
    datecreated = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    result = db.Column(db.Integer)
    timetaken = db.Column(db.Integer)

    def __repr__(self):
        return '<Record user {}, test id {}, question id {}, result: {}>'.format(self.userid,self.testid,self.questionid,self.result)
    
    def asdict(self):
        return {'id':self.id,'userid':self.userid,'testid':self.testid,'questionid':self.questionid,'response':self.response,'result':self.result}

    def __iter__(self):
        yield 'id', self.id
        yield 'userid', self.userid
        yield 'testid', self.testid
        yield 'questionid', self.questionid
        yield 'response', self.response
        yield 'result', self.result

@login.user_loader
def load_user(id):
    return User.query.get(int(id))