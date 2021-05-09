# config.py


import os


class BaseConfig(object):
    SECRET_KEY = '\xe1\xe1\xb7\x1b|\xf2-\xfd0C\x02\x0b\xee\xd0R\xe8\xf5\xa5\xfcK\x00\xfe=\xeb'
    DEBUG = True
    DB_NAME = 'sis_web'
    DB_USER = 'sis_web'
    DB_PASS = '123'
    DB_SERVICE = '172.17.0.2'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )


# class BaseConfig(object):
#     SECRET_KEY = 'hi'
#     DEBUG = True
#     DB_NAME = 'postgres'
#     DB_SERVICE = 'localhost'
#     DB_PORT = 5432
#     SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}/{2}'.format(
#         DB_SERVICE, DB_PORT, DB_NAME
#     )
