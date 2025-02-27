from flask import request,redirect
from api.models.forgetPasswordModel import ForgetPassword
from common.common import apiResponse
from flask_mail import Message,Mail
from app import app

def forgetpassword():
    email=request.form['email']
    forgetpassword=ForgetPassword()
    reset_token=forgetpassword.forgetpassword(email)
    if reset_token!=-1:
        reset_link=request.url_root+"reset-password/"+reset_token
        mail=Mail(app)
        message=Message(
            subject="Reset Password For Flask Application",
            sender="abcx40787@gmail.com",
            recipients=[email],
            html=f"<h3>Hey {email},</h3> <h4>Your Reset-Password Link is here <a href={reset_link}>Click Link </a> </h4>"
        )
        mail.send(message)
        return apiResponse(True,"Mail sent to your email successfully")
    else:
        return apiResponse(False,"User Doesn't Exist!!","")

def resetpassword(reset_token):
    forgetpassword=ForgetPassword()
    updatedpassword=request.form['password']
    print("password-------------",updatedpassword)
    data=forgetpassword.resetpassword(updatedpassword,reset_token)
    if data:
        try:
            return apiResponse(False,data["message"])
        except:
            redirect("/")
            return apiResponse(True,"Password Updated Successfully")
    else:
        return apiResponse(False,"Something went wrong!! please try again!!")

def verifylink(reset_token):
    forgetpassword=ForgetPassword()
    data=forgetpassword.verifylink(reset_token)
    if data==1:
        return apiResponse(True,"Valid Link","")
    else:
        return apiResponse(False,"Invalid Link","")
