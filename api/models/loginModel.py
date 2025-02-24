from sqlalchemy import text
from database import db
from flask import session
import jwt
from datetime import timedelta, datetime
from app import app
from functools import wraps


class Login:
    def login(self, email, password):
        if self.authenticate(email, password) == 0:
            session["logged_in"] = True
            token = jwt.encode(payload={
                'email': email,
                'expiration': str(datetime.utcnow()+timedelta(seconds=120))
            },
                key=app.config['SECRET_KEY'], algorithm='HS256')
            print(token)
            session['token'] = token
            return token
        elif self.authenticate(email, password) == 1:
            return "Wrong Password!!"
        else:
            return "User Not Exist!!"

    def authenticate(self, email, password):
        """Numbering for return statement

        0: user exist
        1: password wrong
        2: user doesn't exist
        """
        queryforuserexist = text("SELECT * FROM USERLOGINREGISTER WHERE email=:email")
        queryforuserexistresult = db.session.execute(queryforuserexist.params(email=email))
        if queryforuserexistresult.fetchone():
            queryforuserpassword = text(
                "SELECT password FROM USERLOGINREGISTER WHERE email=:email and password=:password")
            queryforuserpasswordresult = db.session.execute(
                queryforuserpassword, {'email': email, 'password': password})
            if queryforuserpasswordresult.fetchone():
                return 0
            else:
                return 1
        else:
            return 2

