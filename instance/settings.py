import os

HELLO = 'Hello from instance file'

# DEBUG = False

# celery
CELERY_BROKER_URL = f"redis://:{os.getenv('REDIS_PWD')}" \
                    f"@{os.getenv('REDIS_HOST')}:6379/0"

CELERY_RESULT_BACKEND = f"redis://:{os.getenv('REDIS_PWD')}" \
                        f"@{os.getenv('REDIS_HOST')}:6379/0"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# SQLAlchemy
db_uri = f"postgresql://{os.getenv('SNAKEEYES_DB_USER')}"\
         f":{os.getenv('SNAKEEYES_DB_PWD')}@"\
         f"{os.getenv('SNAKEEYES_HOST')}:5432/snakeeyes'"
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# postgres
# UFWUtKNpKqUgWiz5Svjw
# snakeeyesredispwd
# master.snakeeyes-redis.qljw4m.use1.cache.amazonaws.com
# snakeeyes-db.cp86vwbp9hco.us-east-1.rds.amazonaws.com
