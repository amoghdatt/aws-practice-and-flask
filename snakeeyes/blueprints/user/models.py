import datetime
from collections import OrderedDict
from hashlib import md5

import pytz
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from itsdangerous import URLSafeTimedSerializer, \
     TimedJSONWebSignatureSerializer
from lib.util_sqlalchemy import ResourceMixin, AwareDateTime
from snakeeyes.extensions import db


class User(UserMixin, ResourceMixin, db.Model):
    ROLE = OrderedDict([
        ('member', 'Member'),
        ('admin', 'Admin')
    ])

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # Authentication
    role = db.Column(db.Enum(*ROLE, name='role_types', native_enum=False),
                     index=True, nullable=False, server_default='member')
    active = db.Column('is_active', db.Boolean(), nullable=False,
                       server_default='1')
    username = db.Column(db.String(24), unique=True, index=True)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False,
                      server_default='')
    password = db.Column(db.String(128), nullable=False, server_default='')

    # Activity Tracking
    sign_in_count = db.Column(db.Integer, nullable=False, default=0)
    current_sign_in_on = db.Column(AwareDateTime())
    last_sign_in_on = db.Column(AwareDateTime())
    current_sign_in_ip = db.Column(db.String(45))
    last_sign_in_ip = db.Column(db.String(45))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

        self.password = User.encrypt_password(kwargs.get('password', ''))

    @classmethod
    def find_by_identity(cls, identity):
        return User.query.filter(
            (User.email == identity) | (User.username == identity)
        ).first()

    @classmethod
    def encrypt_password(cls, plaintext_password):
        if plaintext_password:
            return generate_password_hash(plaintext_password)

        return None

    @classmethod
    def deserialize_token(cls, token):
        private_key = TimedJSONWebSignatureSerializer(
                      current_app.config['SECRET_KEY'])
        try:
            decoded_payload = private_key.loads(token)
            return User.find_by_identity(decoded_payload.get('user_email'))
        except Exception:
            return None

    def is_active(self):
        return self.active

    def get_auth_token(self):
        private_key = current_app.config['SECRET_KEY']

        serializer = URLSafeTimedSerializer(private_key)
        data = [str(self.id), md5(self.password.encode('utf-8')).hexdigest()]

        return serializer.dumps(data)

    def authenticated(self, with_password=True, password=''):
        if with_password:
            return check_password_hash(self.password, password)

        return True

    def update_activity_tracking(self, ip_address):
        self.sign_in_count += 1
        self.last_sign_in_on = self.current_sign_in_on
        self.current_sign_in_on = datetime.datetime.now(pytz.utc)
        self.last_sign_in_ip = self.current_sign_in_ip
        self.current_sign_in_ip = ip_address

        return self.save()

    def serialize_token(self, expiration=3600):
        """
        Sign and create a token that can be used for things such as resetting
        a password or other tasks that involve a one off token.

        :param expiration: Seconds until it expires, defaults to 1 hour
        :type expiration: int
        :return: JSON
        """
        private_key = current_app.config['SECRET_KEY']

        serializer = TimedJSONWebSignatureSerializer(private_key, expiration)
        return serializer.dumps({'user_email': self.email}).decode('utf-8')
