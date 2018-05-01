import os
# from myblog.__init__ import app
from manager import  app
from myblog.controllers.blog import blog_blueprint


def runserver():
    port = int(os.environ.get('PORT',5000))
    app.run(host='127.0.0.1',port=port)

if __name__ == '__main__':
    # app.register_blueprint(blog_blueprint)
    runserver()