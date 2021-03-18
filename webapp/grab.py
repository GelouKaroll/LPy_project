from flask import Flask
from webapp.model import db, Point, User

import random

def get_user_id(user_name):

    user = User.query.filter(User.login == user_name).first()
    
    return user.id

def grab_point(user_name):
    
    user_real_id = get_user_id(user_name)

    x = random.uniform(0,5)
    y = random.uniform(0,5)

    new_point = Point(user_id=user_real_id, x=x, y=y)
    
    db.session.add(new_point)
    db.session.commit()

    return