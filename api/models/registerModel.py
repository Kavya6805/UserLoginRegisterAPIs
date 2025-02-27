from sqlalchemy import text
from database import db
from common.common import checkPasswordCredentials


class Register:
    def register(self,username,email,phone,role,password):
        try:
            userexist=text("SELECT email FROM USERLOGINREGISTER WHERE email=:email")
            result=db.session.execute(userexist.params(email=email))
            if result.fetchone():
                return -1
            else:
                sql=text("INSERT INTO USERLOGINREGISTER(username,email,phone,role,password) VALUES(:username,:email,:phone,:role,:password)")
                if checkPasswordCredentials(password)==0:
                    return {"message": "Password must be between 8 to 12 characters"}
                elif checkPasswordCredentials(password)==-1:
                    return {"message": "Password must contain minimum 1 Upper, 1 small,1 special charatcter and 1 digit"}
                hashedpass=checkPasswordCredentials(password)
                db.session.execute(sql.params(username=username,email=email,phone=phone,role=role,password=hashedpass))
                db.session.commit()
                return 1                
        except:
              return 0
        
