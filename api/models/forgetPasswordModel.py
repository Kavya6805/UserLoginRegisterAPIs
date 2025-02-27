from sqlalchemy import text
from database import db
from common.common import generate_encrypted_string,checkPasswordCredentials

class ForgetPassword:
    def forgetpassword(self,email):
        sql=text("SELECT CASE WHEN EXISTS (SELECT 1 FROM USERLOGINREGISTER WHERE email=:email) THEN 1 ELSE 0 END AS VerifyUser")
        result=db.session.execute(sql.params(email=email))
        result=result.mappings().all()
        print(result[0]['VerifyUser'])
        if result[0]['VerifyUser']==1:
            reset_token=generate_encrypted_string()
            updatetokensql=text("UPDATE USERLOGINREGISTER SET reset_token=:reset_token WHERE email=:email")
            db.session.execute(updatetokensql.params(email=email,reset_token=reset_token))
            db.session.commit()
            return reset_token
        else:
            return -1
        
    def verifylink(self,reset_token):
        sql=text("SELECT CASE WHEN EXISTS (SELECT reset_token FROM USERLOGINREGISTER WHERE reset_token=:reset_token)THEN 1 ELSE 0 END as tokenexist ")
        result=db.session.execute(sql.params(reset_token=reset_token))
        result=result.mappings().all()
        print(result[0]['tokenexist'])
        return result[0]['tokenexist']
    
    def resetpassword(self,updatedpassword,reset_token):
        try:
            if checkPasswordCredentials(updatedpassword)==0:
                return {"message": "Password must be between 8 to 12 characters"}
            elif checkPasswordCredentials(updatedpassword)==-1:
                return {"message": "Password must contain minimum 1 Upper, 1 small,1 special charatcter and 1 digit"}
            else:
                hashed_password=checkPasswordCredentials(updatedpassword)
                sql=text("UPDATE USERLOGINREGISTER SET password=:password,reset_token=NULL WHERE reset_token=:reset_token")
                db.session.execute(sql.params(reset_token=reset_token,password=hashed_password))
                db.session.commit()
                return 1
        except:
            return -1
