from sqlalchemy import text
from database import db
from flask import session
import jwt
from datetime import timedelta,datetime
from app import app
from functools import wraps

class Login:
    def login(self,username,password):
        if self.authenticate(username,password):
            session["logged_in"]=True
            token=jwt.encode(payload={
                'username':username,
                'expiration':str(datetime.utcnow()+timedelta(seconds=120))
            },
            key=app.config['SECRET_KEY'],algorithm='HS256')
            print(token)
            session['token']=token
            return token
        else:
            return None

    def authenticate(self,username,password):
        sql=text("SELECT * FROM USERSLOGINREGISTER WHERE username=:username and password=:password")
        result=db.session.execute(sql.params(username=username,password=password))
        if result.fetchone():
            return True
        else:
            return False
        
    def auth(self,func):
        @wraps(func)
        def decorated(*args,**kwargs):
            token=session['token']
            if not token:
                pass
            else:
                pass


