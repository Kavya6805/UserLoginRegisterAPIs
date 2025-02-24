from flask import Flask
from config import DevelopmentConfig
import database

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
database.init_app(app)


from api import bp as apibp

app.register_blueprint(apibp)

@app.route('/')
def index():
    print("Hello",app.config['DEBUG'])
    return "hello"

if __name__=="__main__":
    app.run(debug=True)

