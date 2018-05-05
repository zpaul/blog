# import Flask Script object
import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from myblog import models, __init__,create_app

#Get the env from os_environ
env = os.environ.get('BLOG_ENV','dev')
#Create app instance via factory method
app = create_app('myblog.config.%sConfig' % env.capitalize())
#Init manager
manager = Manager(app)

migrate = Migrate(app,models.db)

# Init manager object via app object
# manager = Manager(__init__.app)

# Init migrate object via app and db object
# migrate = Migrate(__init__.app, models.db)

# Create some new commands
manager.add_command("server", Server())
manager.add_command("db",MigrateCommand)

@manager.shell
def make_shell_context():
    """Create a python CLI.
    return: Default import object
    type: `Dict`
    """
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag,
                Serve=Server)

if __name__ == '__main__':
    manager.run()