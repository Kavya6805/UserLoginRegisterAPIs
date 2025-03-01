from sqlalchemy import text
from database import db
from flask import session
import jwt
from datetime import timedelta, datetime
from app import app
from functools import wraps
from common.common import checkPasswordCredentials

class Login:
    def login(self, email, password):
        if self.authenticate(email, password) == 1:
            session["logged_in"] = True
            token = jwt.encode(payload={
                'email': email,
                'expiration': str(datetime.now()+timedelta(seconds=120))
            },
                key=app.config['SECRET_KEY'], algorithm='HS256')
            print(token)
            session['token'] = token
            return token
        elif self.authenticate(email, password) == 0:
            return 0
        else:
            return -1

    def authenticate(self, email, password):
        """Numbering for return statement

        0: password wrong
        1: user credential fullfilled
        -1: user doesn't exist
        """
        queryforuserexist = text("SELECT * FROM USERLOGINREGISTER WHERE email=:email")
        queryforuserexistresult = db.session.execute(queryforuserexist.params(email=email))
        if queryforuserexistresult.fetchone():
            hashedpassword=checkPasswordCredentials(password)
            queryforuserpassword = text(
                "SELECT password FROM USERLOGINREGISTER WHERE email=:email and password=:password")
            queryforuserpasswordresult = db.session.execute(
                queryforuserpassword, {'email': email, 'password': hashedpassword})
            if queryforuserpasswordresult.fetchone():
                return 1
            else:
                return 0
        else:
            return -1

