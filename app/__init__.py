from flask import Flask 
from .config import Config
from .db import db,migrate
from .models import *

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)


    return app
