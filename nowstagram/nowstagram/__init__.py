# -*- encoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.config.from_pyfile('app.conf')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')#break的拓展
db=SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view='/regloginpage'

app.secret_key = 'nowcoder'
from nowstagram import models,views