#! /usr/bin/env python
# -*- coding: utf-8 -*-

from schema import *


input_user_data = {
    'id': '12',
    'degree': 3,
    'name': '刘大力',
    'email': 'powerfulio@moremom.com',
    'mobile': '13312345679',
    'avatar': 'https://www.baidu.com',
    'money': 1234567,
    'baby_list': [
        dict(nickname='秦琼', age=22),
        dict(nickname='小可爱', age=2)
    ]
}

try:
    obj = UserSchema().load(input_user_data)
    print(obj.name, obj.mobile, obj.money, obj.baby_list[0].nickname)
except marshmallow.ValidationError as err:
    marshmallow.pprint({'errors': err.messages})
