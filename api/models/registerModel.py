from sqlalchemy import text
from database import db


class Register:
    def register(self,username,email,phone,role,password):
        try:
            sql=text("INSERT INTO USERLOGINREGISTER(username,email,phone,role,password) VALUES(:username,:email,:phone,:role,:password)")
            db.session.execute(sql.params(username=username,email=email,phone=phone,role=role,password=password))
            db.session.commit()
            return 1
        except:
            return 0
        
