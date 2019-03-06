from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer,primary_key = True)
        username = db.Column(db.String(255),index = True)
        email = db.Column(db.String(255),unique = True,index = True)
        post = db.relationship('Post',backref = 'user',lazy="dynamic") 

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



class Post(db.Model):
        __tablename__ ='posts'    

        id = db.Column(db.Integer,primary_key = True)
        title= db.Column(db.String(50))
        content= db.Column(db.String(400)) 
        comment_id= db.relationship('Comment',backref = 'posts',lazy="dynamic")  
        user_id = db.Column(db.Integer,db.ForeignKey('users.id'))  
        

    


        def save_post(self):
            db.session.add(self)
            db.session.commit()


        @classmethod
        def clear_post(cls):
            Post.all_posts.clear()

        @classmethod
        def get_posts(id):
            posts= Post.query.all()
            return posts

        def delete_post(self):
            db.session.delete(self)
            db.session.commit()





class Comment(db.Model):
        __tablename__ ='comments'

        id = db.Column(db.Integer,primary_key = True)
        comment = db.Column(db.String(400))
        # user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        post_id= db.Column(db.Integer,db.ForeignKey('posts.id'))


        def save_comment(self):
            db.session.add(self)
            db.session.commit()

        @classmethod
        def get_comment(self,id):

            comment= Comment.query.filter_by(post_id=id).all()     

            return comment



class Quote:
        '''
        Quote class to define Quote Objects
        '''

        def __init__(self,author,id,quote):
            self.author =author
            self.id =id
            self.quote = quote






class Subscriber(UserMixin, db.Model):
   __tablename__="subscribers"

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255))
   email = db.Column(db.String(255),unique = True,index = True)


   def save_subscriber(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_subscribers(cls,id):
       return Subscriber.query.all()


   def __repr__(self):
       return f'User {self.email}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





