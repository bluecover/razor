# -*- coding: utf-8 -*-

''' Generated codes

Marshmallow schema classes accord with model definitions in Swagger.
BE VERY CAREFUL to change this file manually.

'''

import marshmallow


''' SCHEMAS FROM QUERY PARAMETERS.
'''

class ParamUserInfoPreset(object):
    __slots__ = ['child_born', 'child_birth_ts', 'child_gender', 'child_relation', 'child_nickname', '_original_data']

    def __init__(self, child_born, child_gender, child_relation, child_birth_ts=None, child_nickname=None, original_data=None):
        self.child_born = child_born
        self.child_birth_ts = child_birth_ts
        self.child_gender = child_gender
        self.child_relation = child_relation
        self.child_nickname = child_nickname
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamUserInfoPresetSchema(marshmallow.Schema):
    child_born = marshmallow.fields.Integer(required=True)  # 孩子是否已出生 1
    child_birth_ts = marshmallow.fields.Integer()  # 孩子出生日期 时间戳 北京时间 1523264525
    child_gender = marshmallow.fields.Integer(required=True)
    child_relation = marshmallow.fields.Integer(required=True)  # 用户和孩子的关系 2
    child_nickname = marshmallow.fields.String()  # 孩子的昵称 卖马的秦琼

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamUserInfoPreset(**data)
        return obj


''' SCHEMAS FROM MODEL DEFINITIONS.
'''

class UserRussell_(object):
    __slots__ = ['love', 'hatred', '_original_data']

    def __init__(self, love, hatred=None, original_data=None):
        self.love = love
        self.hatred = hatred
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserRussell_Schema(marshmallow.Schema):
    love = marshmallow.fields.String(required=True, missing='wise')  # example: wise
    hatred = marshmallow.fields.String(missing='foolish')  # example: foolish

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserRussell_(**data)
        return obj


class Baby(object):
    __slots__ = ['nickname', 'age', '_original_data']

    def __init__(self, nickname=None, age=None, original_data=None):
        self.nickname = nickname
        self.age = age
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class BabySchema(marshmallow.Schema):
    nickname = marshmallow.fields.String()  # 昵称example: powerfulio
    age = marshmallow.fields.Integer()  # example: 1

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = Baby(**data)
        return obj


class User(object):
    __slots__ = ['id', 'name', 'mobile', 'degree', 'email', 'avatar', 'money', 'baby_list', 'Russell', '_original_data']

    def __init__(self, id, name, mobile, degree, baby_list, email=None, avatar=None, money=None, Russell=None, original_data=None):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.degree = degree
        self.email = email
        self.avatar = avatar
        self.money = money
        self.baby_list = baby_list
        self.Russell = Russell
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserSchema(marshmallow.Schema):
    id = marshmallow.fields.String(required=True)  # 用户 IDexample: 123
    name = marshmallow.fields.String(required=True)  # 姓名example: 刘大力
    mobile = marshmallow.fields.String(required=True)  # example: 18612250030
    degree = marshmallow.fields.Integer(required=True)  # 学历example: 1
    email = marshmallow.fields.String()  # 邮箱
    avatar = marshmallow.fields.String()  # 头像
    money = marshmallow.fields.Decimal()
    baby_list = marshmallow.fields.List(marshmallow.fields.Nested(BabySchema()), required=True)
    Russell = marshmallow.fields.Nested(UserRussell_Schema())

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = User(**data)
        return obj
