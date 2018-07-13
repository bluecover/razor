#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import marshmallow


def mobile(phone_number):
    if not phone_number:
        return False
    p = re.compile(r'^1[3|4|5|8|7]\d{9}$')
    m = p.match(phone_number)
    if not m:
        raise marshmallow.ValidationError('Not a valid mobile.')


class DictObject(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Baby(object):
    __slots__ = ['nickname', 'age', '_data']

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age


class User(object):

    __slots__ = ['id', 'name', 'mobile', 'degree', 'avatar', 'money', 'email', 'baby_list', '_data']

    def __init__(self, id, name, mobile, degree, avatar, money, baby_list, email=None):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.degree = degree
        self.avatar = avatar
        self.money = money
        self.email = email
        self.baby_list = baby_list


class BabySchema(marshmallow.Schema):
    nickname = marshmallow.fields.String(required=True)
    age = marshmallow.fields.Integer(required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, origin_data):
        obj = Baby(**data)
        obj._data = origin_data
        return obj


class UserSchema(marshmallow.Schema):
    id = marshmallow.fields.String(required=True, validate=marshmallow.validate.Length(min=2, max=6))
    name = marshmallow.fields.String(required=True, missing='powerfulio')
    mobile = marshmallow.fields.String(required=True, validate=mobile)
    degree = marshmallow.fields.String()
    email = marshmallow.fields.Email()
    avatar = marshmallow.fields.URL()
    money = marshmallow.fields.Decimal()
    baby_list = marshmallow.fields.List(marshmallow.fields.Nested(BabySchema()))

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, origin_data):
        obj = User(**data)
        obj._data = origin_data
        return obj


degree_int2cn = {
    1: '高中',
    2: '学士',
    3: '硕士',
    4: '博士'
}

input_user_data = {
    'id': '12',
    'degree': '博士',
    'name': '刘大力',
    # 'email': 'powerfulio@moremom.com',
    'mobile': '13312345679',
    'avatar': 'https://www.baidu.com',
    'money': 1234567,
    'baby_list': [
        dict(nickname='秦琼', age=22),
        dict(nickname='小可爱', age=2)
    ]
}


def test_load():
    try:
        data = UserSchema().load(input_user_data)
        marshmallow.pprint(data)
    except marshmallow.ValidationError as err:
        marshmallow.pprint({'errors': err.messages})

    return data


def test_dump():
    try:
        schema = UserSchema()
        result = schema.dump(input_user_data)
        marshmallow.pprint(result)
    except marshmallow.ValidationError as err:
        marshmallow.pprint({'errors': err.messages})


if __name__ == '__main__':
    user = test_load()

    print(user._data)

    print(user.id)
    print(user.name)
    print(user.mobile)
    print(user.email)

    # test_dump()
