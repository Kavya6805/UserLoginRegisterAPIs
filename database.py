from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import Session

db=SQLAlchemy()

def init_app(app):
    db.init_app(app)
    DbSession=Session(db)
    with app.app_context():
        db.Model.metadata.reflect(db.engine,extend_existing=True)