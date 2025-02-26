from flask import Flask,render_template,request
from config import DevelopmentConfig
import database
from flask_mail import Mail
import os
from dotenv import load_dotenv
import requests

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
database.init_app(app)


from api import bp as apibp

app.register_blueprint(apibp)

load_dotenv()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']="abcx40787@gmail.com"
app.config['MAIL_PASSWORD']="amcn invv srsq jnxp"
print(app.config['MAIL_PASSWORD'])
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False

@app.route('/')
def index():
    print("Hello",app.config['DEBUG'])
    return "hello"

@app.route('/reset-password/<reset_token>')
def resetpass(reset_token):
    url=request.url_root+"api/verifylink/"+reset_token
    print(url)
    response=requests.get(url)
    if response.status_code==200:
        response=response.json()
        if response['status']:
            return render_template('reset_password.html',reset_token=reset_token)
        else:
            return response['message']

if __name__=="__main__":
    app.run(debug=True)

