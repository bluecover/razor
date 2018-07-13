#! /usr/bin/env python
# -*- coding: utf-8 -*-

import marshmallow
import emoji
from sanic import Sanic, response
from sanic.response import json

import re
import datetime
import decimal
import collections

from marshmallow.fields import Validator
from marshmallow import validate, ValidationError
from hashlib import sha256

import base64
import jinja2

from signature import VerifySignature


class Mobile(marshmallow.fields.Validator):
    default_message = 'Not a valid mobile number.'

    def __init__(self, error=None):
        self.error = error or self.default_message

    def _format_error(self, value):
        return self.error.format(input=value)

    def __call__(self, value):
        phone_number = value
        if not phone_number:
            return 1
        p = re.compile(r'^1[3|4|5|8|7]\d{9}$')
        m = p.match(phone_number)
        if m:
            return 0
        raise ValidationError(Mobile.default_message)


class JobSchema(marshmallow.Schema):
    company = marshmallow.fields.String(required=True)
    start_date = marshmallow.fields.DateTime(required=True)

class BabySchema(marshmallow.Schema):
    name = marshmallow.fields.String(required=True)
    age = marshmallow.fields.Integer(required=True)

class UserSchema(marshmallow.Schema):
    name = marshmallow.fields.String(required=True)
    mobile = marshmallow.fields.String(required=True, validate=Mobile())
    email = marshmallow.fields.Email(required=True)
    job = marshmallow.fields.Nested(JobSchema(), required=True)
    babies = marshmallow.fields.List(marshmallow.fields.Nested(BabySchema()), required=True)
    married = marshmallow.fields.Boolean(required=True)
    money = marshmallow.fields.Decimal(places=2)
    status = marshmallow.fields.Integer(required=True)
    skills = marshmallow.fields.List(marshmallow.fields.String())
    emoji = marshmallow.fields.List(marshmallow.fields.String())


'''[]
emoji_1 = emoji.emojize('Python is :thumbs_up_sign:')
emoji_2 = emoji.emojize('Python is :thumbsup:', use_aliases=True)

job = dict(
    company = '摩尔妈妈',
    start_date = datetime.datetime(2018, 3, 1)
)
baby_1 = dict(name='zhaohao', age=31)
baby_2 = dict(name='古瑞替', age=10)

user = dict(
    name = '刘大力',
    mobile = '13311234567',
    email = 'zhaohao@moremom.com',
    job = job,
    babies = [baby_1, baby_2],
    married = False,
    money = decimal.Decimal(321.1235678),
    status = -1,
    skills = ['吐槽', '使劲吐槽', ''],
    emoji = [emoji_1, emoji_2]
)

schema = UserSchema()

try:
    result = schema.load(user)
    marshmallow.pprint(result, indent=4)
except ValidationError as ve:
    for field in ve.field_names:
        print(field, ve.data[field])
'''

SALT = '棘心夭夭，母氏劬劳。母氏圣善，我无令人。'

app = Sanic()

@app.route('/get')
async def test_get(request):

    emoji_1 = emoji.emojize('Python is :thumbs_up_sign:')
    emoji_2 = emoji.emojize('Python is :thumbsup:', use_aliases=True)

    job = dict(
        company = '摩尔妈妈',
        start_date = datetime.datetime(2018, 3, 1)
    )
    baby_1 = dict(name='zhaohao', age=31)
    baby_2 = dict(name='古瑞替', age=10)

    user = dict(
        name = '刘大力',
        mobile = '13311234567',
        email = 'zhaohao@moremom.com',
        job = job,
        babies = [baby_1, baby_2],
        married = False,
        money = decimal.Decimal(321.1235678),
        status = -1,
        skills = ['吐槽', '使劲吐槽', ''],
        emoji = [emoji_1, emoji_2]
    )

    schema = UserSchema()
    result = schema.dump(user)

    marshmallow.pprint(result, indent=4)

    return json(result)


@app.post('/post')
async def test_post(request):
    data = UserSchema()
    marshmallow.pprint(request.json)
    result = data.load(request.json)
    marshmallow.pprint(result, indent=4)
    return json(result)


@app.route('/sign')
@app.post('/sign')
async def sign(request):
    h = request.headers
    headers = {
        'token': h.get('token', ''),
        'uuid': h.get('uuid', ''),
        'sid': h.get('sid', ''),
        'ts': h.get('ts', '')
    }
    header_s = '{}{}{}'.format(
        headers.get('token', ''),
        headers.get('uuid', ''),
        headers.get('sid', '')
    )

    ordered_args = collections.OrderedDict()
    for k in sorted(request.raw_args):
        if k != 'sign':
            ordered_args[k] = request.raw_args[k]

    query_s = '&'.join(['{}={}'.format(k, v) for k, v in ordered_args.items()])

    if request.method == 'GET':
        whole = SALT + header_s + query_s + headers['ts']
    else:
        body_s = request.body.decode('utf-8')
        whole = SALT + header_s + query_s + body_s + headers['ts']

    hashed = sha256()
    hashed.update(bytes(whole, encoding='utf8'))
    sign_ = hashed.hexdigest().upper()

    hashed2 = sha256()
    hashed2.update(bytes(sign_, encoding='utf8'))
    sign2_ = hashed2.hexdigest().upper()

    verified = VerifySignature(request)
    assert verified

    t = '''
    <html><body>
        <h1>{{verified}}</h1>
        <h1> Query </h1>
        {% for k, v in query.items() %}
            <h3>{{k}}:{{v}}</h3>
        {% endfor %}
        <h1> Header </h1>
        {% for k, v in header.items() %}
            <h3>{{k}}:{{v}}</h3>
        {% endfor %}
        <h1> Data In Hash </h1>
        <h3>{{data}}</h3>
        <h2>Client: {{ client_sign }}</h2>
        <h2>Server_1: {{ server_sign1 }}</h2>
        <h2>Server_2: {{ server_sign2 }}</h2>
    </html></body>
    '''

    return response.html(body=jinja2.Template(t).render(
        verified=verified,
        query=ordered_args,
        header=headers,
        data=whole, client_sign=h['sig'], server_sign1=sign_, server_sign2=sign2_
    ))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
