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









