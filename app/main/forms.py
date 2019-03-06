from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class QuestionForm(FlaskForm):

    question = StringField('The Question')  
    image_path=StringField('The image')
    submit = SubmitField('Submit')

 

    
# class UpdateProfile(FlaskForm):
#     pitch = TextAreaField('Pitch for yourself',validators = [Required()])
#     submit = SubmitField('Submit')


# class PostForm(FlaskForm):

#     title = StringField('Post title',validators=[Required()])
#     content = TextAreaField('Post Content', validators=[Required()])
#     submit = SubmitField('Submit')

# class CommentForm(FlaskForm):
#     comment = StringField('comment',validators=[Required()])
#     submit = SubmitField('Submit')

# class SubscriberForm(FlaskForm):
#     name = StringField("Enter your name")
#     email = StringField("Email", validators=[Required()])
#     submit= SubmitField('Subscribe')

