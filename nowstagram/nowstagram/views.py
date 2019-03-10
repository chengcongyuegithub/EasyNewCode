#-*- encoding=UTF-8 -*-

from models import Image,User
from nowstagram import app,db
from flask import render_template,redirect

@app.route('/')
def index():
    images =Image.query.order_by(db.desc(Image.id)).limit(10).all()
    print 1,images
    return render_template('index.html',images=images)