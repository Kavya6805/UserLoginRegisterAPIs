from sqlalchemy import URL
from datetime import timedelta

DATABASE_HOST="localhost"
DATABASE_NAME="flask_restapi"
DATABASE_USERNAME="root"
DATABASE_PASSWORD=""

CONN_URL=URL.create(
    "mysql+pymysql",
    username=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=3306,
    database=DATABASE_NAME
)
print(CONN_URL)

class Config:
    DEBUG=True
    SECRET_KEY='78cdbb7fd37443df82a37cde309d1676'
    # for secret key we use 
    #  import uuid
    # uuid.uuid4().hex
    SQLALCHEMY_DATABASE_URI=CONN_URL
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(Config):
    DEBUG=True
    ENV='development'
    DEVELOPMENT=True
    SQLALCHEMY_ECHO=False

class ProductionConfig(Config):
    DEBUG=False

