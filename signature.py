# -*- coding: utf-8 -*-

''' Verify request signature
    验证客户端请求的签名

哈希算法
    SHA-256

参与哈希的字段 !必须严格按照如下顺序拼接
    salt: 盐 在最前
    header: 以下几个字段的 value 按如下顺序拼接, key 不参与哈希
        - header['token']
        - header['uuid']
        - header['sid']
    query:
        对所有 key=value 键值对按照 key 的 "字典顺序" 升序排序后拼接
    body:
        直接作为字符串拼接
    timestamp：
        时间戳 header['ts'] 放在最后

哈希前数据
    plain_data = salt + header + query + body + timestamp
    样例: 这是一把使用汉字的盐TokenABCUuid123Sid567-p1=value1&p2=value2{"name":"\u5218\u5927\u529b","money":321.12,,"email":"zhaohao@moremom.com","mobile":"13311234567"}1521710099068

哈希过程:
    执行两次 SHA-256 每次结果字母都使用 Uppercase
    hash = SHA-256(SHA-256(plain_data).upper()).upper()

'''

import collections
from hashlib import sha256


def BuildSignature(header, query, body, salt) -> str:
    header_data = '{token}{uuid}{sid}'.format(
        token=header['token'],
        uuid=header['uuid'],
        sid=header['sid']
    )

    ordered_query = collections.OrderedDict()
    for k in sorted(query.keys()):
        ordered_query[k] = query[k]
    query_data = '&'.join(['{}={}'.format(k, v) for k, v in ordered_query.items()])

    plain = salt + header_data + query_data + body + header['ts']

    hasher = sha256()
    hasher.update(bytes(plain, encoding='utf8'))
    signature_1 = hasher.hexdigest().upper()
    hasher.update(bytes(signature_1, encoding='utf8'))
    signature_2 = hasher.hexdigest().upper()

    return signature_2


SALT = 'SALT'


def VerifySignature(request) -> bool:
    body_str = request.body.decode('utf-8')
    server_signature = BuildSignature(request.headers, request.raw_args, body_str, SALT)
    server_signature = request.headers['sig']
    return server_signature == server_signature
