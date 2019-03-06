from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True,index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    score_id= db.Column(db.Integer,db.ForeignKey('scores.id')) 
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    # joint=db.relationship('Joint',backref ='users',lazy="dynamic")

    

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):         
        return f'User {self.username}'

    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)




class Score(db.Model):
    __tablename__ ='scores'

    id = db.Column(db.Integer,primary_key = True)
    score = db.Column(db.String(255))
    user_id = db.relationship('User',backref ='scores',lazy="dynamic")


    @classmethod
    def get_scores(id):

        scores= Score.query. filter_by(user_id)

        return scores





class Question(db.Model):
    __tablename__ ='questions'

    id = db.Column(db.Integer,primary_key = True)
    question = db.Column(db.String(100))
    answers = db.relationship('Answer',backref ='questions',lazy="dynamic")

    

class Answer(db.Model):
    __tablename__ ='answers'

    id = db.Column(db.Integer,primary_key = True)
    answer = db.Column(db.String(100))
    mark = db.Column(db.Integer())
    question_id = db.Column(db.Integer,db.ForeignKey('questions.id'))
    # joint=db.relationship('Joint',backref ='answers',lazy="dynamic")

    def save_answer(self):
        db.session.add(self)
        db.session.commit()

    def get_answer(self):
        answer.query.filter_by(id)
 

Joint = db.Table('joints',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answers.id'), primary_key=True)
)




# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags, lazy='subquery',
#         backref=db.backref('pages', lazy=True))

# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


# class Joint(db.Model):

#     __tablename__ ='joints'

#     id = db.Column(db.Integer,primary_key = True)
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id')) 
#     answer_id = db.Column(db.Integer,db.ForeignKey('answers.id'))




 

 










 