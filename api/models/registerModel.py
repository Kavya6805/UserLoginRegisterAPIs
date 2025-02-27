from sqlalchemy import text
from database import db
from common.common import checkPasswordCredentials


class Register:
    def register(self,username,email,phone,role,password):
        try:
            sql=text("INSERT INTO USERLOGINREGISTER(username,email,phone,role,password) VALUES(:username,:email,:phone,:role,:password)")
            db.session.execute(sql.params(username=username,email=email,phone=phone,role=role,password=password))
            if checkPasswordCredentials(password)==0:
                return {"message": "Password must be between 8 to 12 characters"}
            elif checkPasswordCredentials(password)==-1:
                return {"message": "Password must contain minimum 1 Upper, 1 small,1 special charatcter and 1 digit"}
            db.session.commit()
            return 1
        except:
            return 0
        
