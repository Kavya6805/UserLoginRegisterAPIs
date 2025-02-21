from sqlalchemy import text
from database import db
from flask import session
import jwt
from datetime import timedelta, datetime
from app import app
from functools import wraps


class Login:
    def login(self, username, password):
        if self.authenticate(username, password) == 0:
            session["logged_in"] = True
            token = jwt.encode(payload={
                'username': username,
                'expiration': str(datetime.utcnow()+timedelta(seconds=120))
            },
                key=app.config['SECRET_KEY'], algorithm='HS256')
            print(token)
            session['token'] = token
            return token
        elif self.authenticate(username, password) == 1:
            return "Wrong Password!!"
        else:
            return "User Not Exist!!"

    def authenticate(self, username, password):
        sql1 = text("SELECT * FROM USERLOGINREGISTER WHERE username=:username")
        result1 = db.session.execute(sql1.params(username=username))
        if result1.fetchone():
            sql2 = text(
                "SELECT password FROM USERLOGINREGISTER WHERE username=:username and password=:password")
            result2 = db.session.execute(
                sql2, {'username': username, 'password': password})
            if result2.fetchone():
                return 0
            else:
                return 1
        else:
            return 2

    def auth(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            token = session['token']
            if not token:
                pass
            else:
                pass
