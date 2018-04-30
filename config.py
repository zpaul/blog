class Config(object):
    """Base config class."""
    SECRET_KEY = 'ZHENYZXB'
class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zhen@localhost:3306/blog?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False