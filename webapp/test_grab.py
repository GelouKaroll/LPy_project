from flask import Flask
from webapp.model import db, Point, User

import random

def get_user_id(login):

    user =  User.query.filter(User.login==login)
    
    return print(user.id)

def grab():
    print('inside grab fnc')
    #user_real_id = get_user_id(login)

    for i in range(0,5):
        x = random.uniform(0,5)
        y = random.uniform(0,5)

        new_point = Point(user_id=user_real_id, x=x, y=y)
        
        db.session.add(new_point)
        db.session.commit()

    return print('from return inside grab fnc')