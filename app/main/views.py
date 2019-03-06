from flask import render_template,redirect,url_for,abort
from . import main  
from ..request import get_onequote 
from ..models import User,Post,Comment,Subscriber,Quote
from flask_login import login_required,current_user
from .. import db,photos 
from .forms import PostForm,CommentForm,SubscriberForm
from ..email import mail_message



# @main.route('/')
# def index():
#     """ View root page function that returns index page
#     """
#     all_posts = Post.get_posts()
#      quote = get_onequote()
 

#     title = 'Welcome to Blog Posts'
#     return render_template('index.html', quote=quote) 



@main.route('/post/new', methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
  
    # movie = get_movie(id)

    if form.validate_on_submit():
        # title = form.title.data
        title= form.title.data
        content = form.content.data
        new_post = Post(user_id=current_user.id,title=title, content=content)
        new_post.save_post()
        return redirect(url_for('.index',content = content))

    # username = f'{user.username} pitch'
    return render_template('new_post.html', post_form=form)


@main.route('/posts')
def display_post():
    all_posts = Post.get_posts()
    print(all_posts)
    return render_template("posts.html",all_posts=all_posts )



@main.route('/posts')
@login_required
def delete_post():
    removedPost = Post.delete_posts()  
    return render_template("posts.html",removedPost=removedPost )



@main.route('/comments/<int:id>', methods = ['GET','POST'])
 
def new_comment(id):
    form = CommentForm()  
    post=Post.query.filter_by(id=id).first()

    if form.validate_on_submit():
        comment = form.comment.data
    
        new_comment = Comment(user_id=current_user.id,post_id=post.id,comment=comment)
        new_comment.save_comment()
        return redirect(url_for('main.index',comment=comment))

    return render_template('comments.html', comment_form=form)


@main.route('/subscribe',methods=["GET","POST"])
def subscriber():
    form=SubscriberForm()

    if form.validate_on_submit():
        subscriber = Subscriber(name=form.name.data,email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()

        mail_message("Welcome to this platform","email/welcome_user",subscriber.email,subscriber=subscriber)
        return redirect(url_for('main.index'))
        title = 'Subscribe'
    return render_template('subscription.html',form=form)


 





 















# @main.route('/quotes/<int:id>')
# def quotes(quote_id):

#     '''
#     View quote page function that returns the quote details page and its data
#     '''
#     return render_template('quotes.html',id = quote_id)

@main.route('/')
def index():

    '''
    View quote page function that returns the quote details page and its data
    '''
    quote = get_onequote()
 

    return render_template('index.html',quote=quote)


 


# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()
#     user.pitch = form.pitch.data
       

#     if form.validate_on_submit():
#         db.session.add(user)
#         db.session.commit()
       

    

#         return redirect(url_for('.profile',uname=user.username))

#     return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

# @main.route('/user/<uname>/update/pitcf',methods= ['POST'])
# @login_required
# def update_pitch(uname):
#     user = User.query.filter_by(username = uname).first()
#     if pitch:
#         # filename = photos.save(request.files['photo'])
#         # path = f'photos/{filename}'
#         # user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

# @main.route('/')
# def index():
#     """ View root page function that returns index page
#     """
     

#     title = 'Home- Welcome'
#     return render_template('index.html', title = title, )









    

 

    

