from sqlalchemy import text
from database import db

class UserList:
    def userlist(self):
        sql=text("SELECT * FROM USERLOGINREGISTER")
        result=db.session.execute(sql)
        return result.mappings().all()