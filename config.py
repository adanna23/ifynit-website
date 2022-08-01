import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
    we will set config variables for flask app here
    using environment variables where available, otherwise
    we will create the config variables if not already done
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off uodate messages from database