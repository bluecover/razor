# -*- coding: utf-8 -*-

from marshmallow import pprint
from schema import UserSchema

import datetime


class Playground:
    def __init__(self):
        self.type = 'inside'


pg = Playground()
print(pg.type)
pg.type = 'outside'
print(pg.type)


if __name__ == '__main__':
    job_data = {
        'company': '摩尔妈妈',
        'start_date': '2018-3-1'
    }
    user_data = {
        'name': '刘大力',
        'mobile': '18612340000',
        'email': 'zh@gmail.com',
        'job': job_data
    }
    user = UserSchema()
    result = user.load(user_data)
    pprint(result)
