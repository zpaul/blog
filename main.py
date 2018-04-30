#coding=utf8
from flask import Flask,url_for,render_template,request
from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)
app.url_map.strict_slashes = False

import views
import wt_forms

# @app.route('/')
# def home(name=None):
#     return render_template('home.html', name=name)
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

