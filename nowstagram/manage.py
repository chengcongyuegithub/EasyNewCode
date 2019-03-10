#-*- encoding=UTF-8 -*-

from nowstagram import app,db
from flask_script import Manager
from nowstagram.models import User,Image,Comment
import random

manager=Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,10):
       db.session.add(User('tianhao'+str(i+1),'a'+str(i+1)))
       for j in range(0, 3):
           db.session.add(Image(get_image_url(), i + 1))
           for k in range(0,3):
              db.session.add(Comment('This is Comment'+str(k),1+3*i+j,i+1))
    db.session.commit()

    #更新
    for i in range(0,10,2):
       User.query.filter_by(id=i+1).update({'username':'newCode'+str(i)})
    for i in range(1,10,2):
        u=User.query.get(i+1)
        u.username='d'+str(i*i)
    db.session.commit()
    #删除
    for i in range(0,10,2):
        Comment.query.filter_by(id=i+1).delete();
    db.session.commit()
    ##查询
    print 1,User.query.all()
    #print 2,User.query.get(3)
    #print 3,User.query.filter_by(id=2).first()
    #print 4,User.query.order_by(User.id.desc()).offset(1),limit(2).all()
    #print 5,User.query.paginate(page=1,per_page=10).items
    u=User.query.get(1)
    #print 6,u
    #print 7,u.images
    #print 8,Image.query.get(1).user
if __name__ == '__main__':
    manager.run()