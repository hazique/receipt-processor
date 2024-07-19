class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    

class TestConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/test_db'
