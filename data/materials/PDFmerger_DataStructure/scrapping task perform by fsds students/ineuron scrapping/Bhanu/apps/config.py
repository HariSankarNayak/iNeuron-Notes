# importing required packages
import os
from decouple import config


# application configuration
class Config(object):
    base_dir = os.path.abspath(os.path.dirname(__file__))

    # set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # this will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# application production environment configuration
class ProductionConfig(Config):
    # set debug flag
    DEBUG = False

    # set security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='postgresql'),
        config('DB_USERNAME', default='ineuron-data'),
        config('DB_PASS', default='pass'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=5432),
        config('DB_NAME', default='ineuron-data-flask')
    )


# application development environment configuration
class DebugConfig(Config):
    # set debug flag
    DEBUG = True


# load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}



