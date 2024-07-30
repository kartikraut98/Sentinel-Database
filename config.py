import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','6b5b3eec348a1e2c6e34bc8b9c87276c09a5e31d47a6f7f5a83c758e6c8746b1')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Frenchfries12345$#')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sentinaldatahub')
    MYSQL_CURSORCLASS = 'DictCursor'
