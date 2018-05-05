#coding=utf8
from flask import Flask, url_for, redirect

# from myblog.config import DevConfig
from myblog.models import db
from myblog.controllers import blog
from myblog.extensions import bcrypt

# app = Flask(__name__)
# app.config.from_object(DevConfig)
# app.url_map.strict_slashes = False
# db.init_app(app)

def create_app(object_name):
    """Create the app instance via factory Method"""

    app = Flask(__name__)
    #set app config
    app.config.from_object(object_name)

    #will load config.py to object
    db.init_app(app)
    #Init the bcrypt via app object
    bcrypt.init_app(app)

    @app.route('/')
    def index():
        #Redirect the url
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog.blog_blueprint)

    return app


# @app.route('/')
# def index():
#     return redirect(url_for('blog.home'))
#
# app.register_blueprint(blog.blog_blueprint)
#
#
#
# @app.route('/home/')
# def home_world():
#     return 'home Flask!'
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>/')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


# with app.test_request_context():
#     print(url_for('home'))
    # print(url_for('show_post',post_id='233 absd'))


# if __name__ == '__main__':
#     # app.debug = True
#     app.run()

