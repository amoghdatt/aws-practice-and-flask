from datetime import timedelta

DEBUG = True

SERVER_NAME = 'ec2-3-222-116-240.compute-1.amazonaws.com:8000'
SECRET_KEY = 'insecurefordev'

# Flask-Mail
MAIL_DEFAULT_SERVER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'me@gmail.com'
MAIL_PASSWORD = 'myawesomepassword'

# celery
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# SQLAlchemy
db_uri = 'postgresql://snakeeyes:devpassword@postgres:5432/snakeeyes'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)