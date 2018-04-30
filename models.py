from flask_sqlalchemy import SQLAlchemy
from main import app

# 定义数据模型

# INIT the sqlalchemy object
# Will be load the SQLALCHEMY_DATABASE_URL from config.py
# SQLAlchemy 会自动的从 app 对象中的 DevConfig 中加载连接数据库的配置项
db = SQLAlchemy(app)


class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # Establish contact with Post's ForeignKey: user_id
    # db.relationsformat(self.username)hip：会在 SQLAlchemy 中创建一个虚拟的列，该列会与 Post.user_id (db.ForeignKey) 建立联系
    # backref用于指定表之间的双向关系，如果在一对多的关系中建立双向的关系,这样的话在对方看来这就是一个多对一的关系。
    # lazy：指定 SQLAlchemy 加载关联对象的方式。
    # lazy=subquery: 会在加载 Post 对象后，将与 Post 相关联的对象全部加载，这样就可以减少 Query 的动作，也就是减少了对 DB 的 I/O 操作。
    # 但可能会返回大量不被使用的数据，会影响效率。
    # lazy=dynamic: 只有被使用时，对象才会被加载，并且返回式会进行过滤，如果现在或将来需要返回的数据量很大，建议使用这种方式。Post 就属于这种对象。
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)


# many to many 的关系仍然是由 db.relationship() 来定义
# seconddary(次级)：会告知 SQLAlchemy 该 many to many 的关联保存在 posts_tags 表中
# backref：声明表之间的关系是双向
# 需要注意的是：在 one to many 中的 backref 是一个普通的对象，而在 many to many 中的 backref 是一个 List 对象。

posts_tags = db.Table('posts_tags',
                      db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
                      db.Column(('tag_id'), db.String(45), db.ForeignKey('tags.id')))


class Post(db.Model):
    """Represents Proected posts."""
    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)

    # set fk for post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    # Establish contact with Comment's ForeignKey: post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic')
    # many to many posts <==>tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return "<Model Post '{}'>".format(self.title)


class Comment(db.Model):
    """docstring for Comment"""
    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, id,name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Comment'{}'>".format(self.name)


class Tag(db.Model):
    """docstring for Tag"""

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, id,name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Tag '{}'>".format(self.name)
