import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #zaštita forme od CSRF napada
    SECRET_KEY = os.environ.get('SECRET_KEY') or ')t2aKlJ_m8ZDbJ;U])EMEZkIgPX+EM4PogX45HCUH.JGC![erd'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    '''MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['matisa.webapp@gmail.com']'''

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'matisa.webapp'
    MAIL_PASSWORD = 'hrgsugdnhdjsvwfo'
    ADMINS = ['matisa.webapp@gmail.com']
