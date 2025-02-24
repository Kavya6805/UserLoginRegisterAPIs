from api.models.userListModel import UserList
from common.common import apiResponse
from common.common import auth

@auth
def userlist():
    try:
        userlist=UserList()
        data=userlist.userlist()
        data=[dict(row) for row in data]
        return apiResponse(True,"Users Found!!",data)
    except:
        return apiResponse(False,"Something Went Wrong!!",None)
