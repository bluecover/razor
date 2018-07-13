# -*- coding: utf-8 -*-

import datetime
from transport import *
import urllib
import collections
from hashlib import sha256
import base64
try:
    from ujson import dumps as json_dumps
except BaseException:
    from json import dumps as json_dumps

def test_sign():
    headers = {
        'token': 'token',
        'uuid': 'uuid',
        'sid': 'sid',
        'ts': str(int(datetime.datetime.now().timestamp() * 1000))
    }
    header_text = '{}{}{}'.format(headers['token'], headers['uuid'], headers['sid'])

    params = {
        'p1': 'value1',
        'p2': 'value2',
        'p3': '#'
    }
    ordered_params = collections.OrderedDict()
    for k in sorted(params.keys()):
        ordered_params[k] = params[k]
    query_text = '&'.join(['{}={}'.format(k, v) for k, v in ordered_params.items()])

    whole_get = SALT + header_text + query_text + headers['ts']

    hashed = sha256()
    hashed.update(bytes(whole_get, encoding='utf8'))
    sig = hashed.hexdigest().upper()
    headers['sig'] = sig

    request, response = app.test_client.get('/sign', params=params, headers=headers)
    assert response.status == 200
    print(response.text)

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
    data = schema.dump(user)
    body = json_dumps(data)
    body_b64 = base64.b64encode(bytes(body, encoding="utf8"))
    body_s = str(body_b64, encoding = "utf-8")

    whole_post = '{}{}{}{}'.format(SALT, header_text, body, headers['ts'])
    hashed = sha256()
    hashed.update(bytes(whole_post, encoding='utf8'))
    sig = hashed.hexdigest().upper()
    headers['sig'] = sig
    _, resp = app.test_client.post('/sign', headers=headers, data=body)
    print(resp.text)


if __name__ == '__main__':
    test_sign()
