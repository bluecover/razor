# -*- coding: utf-8 -*-

''' Generated codes

Marshmallow schema classes accord with model definitions in Swagger.
BE VERY CAREFUL to change this file manually.

'''

import marshmallow
from base import validator


''' SCHEMAS FROM QUERY PARAMETERS.
'''

class ParamHeaderSig(object):
    __slots__ = ['token', 'uuid', 'sid', 'sig', 'ts', 'did', 'dplatform', 'dbrand', 'osv', 'app', 'appv', 'resolution', 'channel', 'ac', '_original_data']

    def __init__(self, token, uuid, sid, sig, ts, did, dplatform, dbrand, osv, app, appv, resolution, channel, ac, original_data=None):
        self.token = token
        self.uuid = uuid
        self.sid = sid
        self.sig = sig
        self.ts = ts
        self.did = did
        self.dplatform = dplatform
        self.dbrand = dbrand
        self.osv = osv
        self.app = app
        self.appv = appv
        self.resolution = resolution
        self.channel = channel
        self.ac = ac
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamHeaderSigSchema(marshmallow.Schema):
    token = marshmallow.fields.String(required=True)  # 由服务器返回； 服务器判断用户是否登录的依据。
    uuid = marshmallow.fields.String(required=True)  # 由APP端生成； sha256( salt + device_id + timestamp + os ) APP安装后，本地产生唯一的 id
    sid = marshmallow.fields.String(required=True)  # 由APP端生成； sha256( salt + device_id + timestamp ) APP每次启动都不一样
    sig = marshmallow.fields.String(required=True)  # sha256( sha256( salt + token + uuid + sid + ...上面的字段...+ ts + query_string + post_body ) ) 每次请求都带
    ts = marshmallow.fields.Integer(required=True)  # timestamp_ts 摘要生成时间
    did = marshmallow.fields.String(required=True)  # 设备唯一id
    dplatform = marshmallow.fields.String(required=True)  # android or iphone
    dbrand = marshmallow.fields.String(required=True)  # 手机品牌 huawei xiaomi ……
    osv = marshmallow.fields.String(required=True)  # 设备安卓或ios系统版本号 7.0 / 11.2.5
    app = marshmallow.fields.String(required=True)  # APP 名字 moremom
    appv = marshmallow.fields.String(required=True)  # APP 版本号
    resolution = marshmallow.fields.String(required=True)  # 设备分辨率
    channel = marshmallow.fields.String(required=True)  # app下载渠道
    ac = marshmallow.fields.String(required=True)  # wife / 4G/ 3G

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamHeaderSig(**data)
        return obj


class ParamAppAd(object):
    __slots__ = ['update_ts', '_original_data']

    def __init__(self, update_ts, original_data=None):
        self.update_ts = update_ts
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamAppAdSchema(marshmallow.Schema):
    update_ts = marshmallow.fields.Integer(required=True)  # 最近一次获取 app init 配置的 时间戳； 服务器根据这个值判断是否下发新配置。

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamAppAd(**data)
        return obj


class ParamAppConfig(object):
    __slots__ = ['update_ts', '_original_data']

    def __init__(self, update_ts, original_data=None):
        self.update_ts = update_ts
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamAppConfigSchema(marshmallow.Schema):
    update_ts = marshmallow.fields.Integer(required=True)  # 最近一次获取 app init 配置的 摘要值； 服务器根据这个值判断是否下发新配置。

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamAppConfig(**data)
        return obj


class ParamAuthMobileCode(object):
    __slots__ = ['mobile', '_original_data']

    def __init__(self, mobile, original_data=None):
        self.mobile = mobile
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamAuthMobileCodeSchema(marshmallow.Schema):
    mobile = marshmallow.fields.String(required=True)  # 明文手机号

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamAuthMobileCode(**data)
        return obj


class ParamOssUploadToken(object):
    __slots__ = ['cloud', 'category', 'user', '_original_data']

    def __init__(self, cloud=None, category=None, user=None, original_data=None):
        self.cloud = cloud
        self.category = category
        self.user = user
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamOssUploadTokenSchema(marshmallow.Schema):
    cloud = marshmallow.fields.String()  # 云服务商 目前只用qiniu qiniu
    category = marshmallow.fields.String()  # 上传文件类别 avatar: 头像 video: 视频 identity: 识别 birth: 出生证
    user = marshmallow.fields.String()  # 用户 ID hello123

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamOssUploadToken(**data)
        return obj


class ParamOssDownloadUrl(object):
    __slots__ = ['cloud', 'domain', 'key', '_original_data']

    def __init__(self, cloud=None, domain=None, key=None, original_data=None):
        self.cloud = cloud
        self.domain = domain
        self.key = key
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamOssDownloadUrlSchema(marshmallow.Schema):
    cloud = marshmallow.fields.String()  # 云服务商 目前只用qiniu
    domain = marshmallow.fields.String()  # 公开的 base URL
    key = marshmallow.fields.String()  # 文件在 OSS 上的 bucket/key 存储路径

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamOssDownloadUrl(**data)
        return obj


class ParamUserCarerInfo(object):
    __slots__ = ['user_id', 'lng', 'lat', '_original_data']

    def __init__(self, user_id, lng=None, lat=None, original_data=None):
        self.user_id = user_id
        self.lng = lng
        self.lat = lat
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamUserCarerInfoSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(required=True)  # 看护人的用户ID 123
    lng = marshmallow.fields.Decimal()  # 经度 116.483765
    lat = marshmallow.fields.Decimal()  # 纬度 39.961914

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamUserCarerInfo(**data)
        return obj


class ParamRecommendCarer(object):
    __slots__ = ['child_born', 'child_birth_ts', 'child_gender', 'child_relation', 'child_nickname', '_original_data']

    def __init__(self, child_born=None, child_birth_ts=None, child_gender=None, child_relation=None, child_nickname=None, original_data=None):
        self.child_born = child_born
        self.child_birth_ts = child_birth_ts
        self.child_gender = child_gender
        self.child_relation = child_relation
        self.child_nickname = child_nickname
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ParamRecommendCarerSchema(marshmallow.Schema):
    child_born = marshmallow.fields.Integer()  # 孩子是否已出生 1
    child_birth_ts = marshmallow.fields.Integer()  # 孩子出生日期 时间戳 北京时间 1523264525
    child_gender = marshmallow.fields.Integer()
    child_relation = marshmallow.fields.Integer()  # 用户和孩子的关系 2
    child_nickname = marshmallow.fields.String()  # 孩子的昵称 卖马的秦琼

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ParamRecommendCarer(**data)
        return obj


''' SCHEMAS FROM MODEL DEFINITIONS.
'''

class Address(object):
    __slots__ = ['lng', 'lat', 'province', 'city', 'district', 'address', 'name', 'room', '_original_data']

    def __init__(self, city, lng=None, lat=None, province=None, district=None, address=None, name=None, room=None, original_data=None):
        self.lng = lng
        self.lat = lat
        self.province = province
        self.city = city
        self.district = district
        self.address = address
        self.name = name
        self.room = room
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class AddressSchema(marshmallow.Schema):
    lng = marshmallow.fields.Decimal()  # example: 116.483765
    lat = marshmallow.fields.Decimal()  # example: 39.961914
    province = marshmallow.fields.String()  # 省份/直辖市example: 北京市
    city = marshmallow.fields.String(required=True)  # 城市example: 北京市
    district = marshmallow.fields.String()  # 区example: 海淀区
    address = marshmallow.fields.String()  # 详细地址example: 张自忠路3号段
    name = marshmallow.fields.String()  # 机构名example: 段祺瑞执政府旧址
    room = marshmallow.fields.String()  # 用户填写的门牌号example: 6号楼3单元202室

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = Address(**data)
        return obj


class AppInitAdData(object):
    __slots__ = ['update_ts', 'adsrc', 'adurl', 'interval', '_original_data']

    def __init__(self, update_ts=None, adsrc=None, adurl=None, interval=None, original_data=None):
        self.update_ts = update_ts
        self.adsrc = adsrc
        self.adurl = adurl
        self.interval = interval
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class AppInitAdDataSchema(marshmallow.Schema):
    update_ts = marshmallow.fields.Integer()  # 更新时间戳
    adsrc = marshmallow.fields.String()  # 广告资源位置
    adurl = marshmallow.fields.String()  # 广告资源跳转
    interval = marshmallow.fields.Integer()  # 广告展示时间

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = AppInitAdData(**data)
        return obj


class AppInitConfigData(object):
    __slots__ = ['update_ts', 'content', 'app_version', '_original_data']

    def __init__(self, update_ts=None, content=None, app_version=None, original_data=None):
        self.update_ts = update_ts
        self.content = content
        self.app_version = app_version
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class AppInitConfigDataSchema(marshmallow.Schema):
    update_ts = marshmallow.fields.Integer()  # 更新时间戳
    content = marshmallow.fields.String()  # 配置的Json字符串
    app_version = marshmallow.fields.Integer()  # 三位数版本号 / 103

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = AppInitConfigData(**data)
        return obj


class AuthMobileCodeResponseData_Data(object):
    __slots__ = ['code', 'mobile', 'retry_time', '_original_data']

    def __init__(self, code=None, mobile=None, retry_time=None, original_data=None):
        self.code = code
        self.mobile = mobile
        self.retry_time = retry_time
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class AuthMobileCodeResponseData_DataSchema(marshmallow.Schema):
    code = marshmallow.fields.Integer()  # 登陆验证码example: 9527
    mobile = marshmallow.fields.String()  # 待登陆手机号example: 13611112222
    retry_time = marshmallow.fields.String()  # retry within xx secondsexample: 2

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = AuthMobileCodeResponseData_Data(**data)
        return obj


class AuthMobileLoginRequest_ChildInfo(object):
    __slots__ = ['born', 'nickname', 'birth_ts', 'gender', 'relation', '_original_data']

    def __init__(self, born=None, nickname=None, birth_ts=None, gender=None, relation=None, original_data=None):
        self.born = born
        self.nickname = nickname
        self.birth_ts = birth_ts
        self.gender = gender
        self.relation = relation
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class AuthMobileLoginRequest_ChildInfoSchema(marshmallow.Schema):
    born = marshmallow.fields.Integer()  # 孩子是否已出生example: 1
    nickname = marshmallow.fields.String()  # 孩子昵称example: powerfulio
    birth_ts = marshmallow.fields.Integer()  # 孩子出生日期 时间戳 北京时间example: 1523264525
    gender = marshmallow.fields.Integer()  # example: 1
    relation = marshmallow.fields.Integer()  # 用户和孩子的关系example: 1

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = AuthMobileLoginRequest_ChildInfo(**data)
        return obj


class AuthMobileLoginResponseData(object):
    __slots__ = ['user_id', 'token', '_original_data']

    def __init__(self, user_id=None, token=None, original_data=None):
        self.user_id = user_id
        self.token = token
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class AuthMobileLoginResponseDataSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(validate=validator.v_enc_id)  # example: uuid_user_1
    token = marshmallow.fields.String()  # Token From Serverexample: token_123ABC

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = AuthMobileLoginResponseData(**data)
        return obj


class CarerApplyResponseData(object):
    __slots__ = ['verify_date', 'qr', 'wx_id', '_original_data']

    def __init__(self, verify_date=None, qr=None, wx_id=None, original_data=None):
        self.verify_date = verify_date
        self.qr = qr
        self.wx_id = wx_id
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class CarerApplyResponseDataSchema(marshmallow.Schema):
    verify_date = marshmallow.fields.String()  # 预计审核完成日期example: 2018-05-01
    qr = marshmallow.fields.URL(relative=True)  # 微信群二维码 URLexample: http://qiniu.com//birth_cert.jpg
    wx_id = marshmallow.fields.String()  # 微信号example: more_fat_gay

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = CarerApplyResponseData(**data)
        return obj


class Child(object):
    __slots__ = ['id', 'nickname', 'realname', 'gender', 'age', 'id_card_no', '_original_data']

    def __init__(self, id=None, nickname=None, realname=None, gender=None, age=None, id_card_no=None, original_data=None):
        self.id = id
        self.nickname = nickname
        self.realname = realname
        self.gender = gender
        self.age = age
        self.id_card_no = id_card_no
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ChildSchema(marshmallow.Schema):
    id = marshmallow.fields.Integer(validate=validator.v_enc_id)  # example: uuid_child_1
    nickname = marshmallow.fields.String()  # 昵称example: powerfulio
    realname = marshmallow.fields.String()  # 真实姓名example: 刘小力
    gender = marshmallow.fields.String()  # example: 女
    age = marshmallow.fields.Integer()  # example: 1
    id_card_no = marshmallow.fields.String()  # 身份证号example: 220324199608192318

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = Child(**data)
        return obj


class ChildUpdateResponseData(object):
    __slots__ = ['id', '_original_data']

    def __init__(self, id=None, original_data=None):
        self.id = id
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ChildUpdateResponseDataSchema(marshmallow.Schema):
    id = marshmallow.fields.String(validate=validator.v_enc_id)  # example: uuid_child_1

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ChildUpdateResponseData(**data)
        return obj


class DataDeviceInfo(object):
    __slots__ = ['uuid', 'device_id', 'device_manufacturer', 'device_platform', 'device_brand', 'device_type', 'app_version', 'os_version', 'os_lang', 'channel', 'resolution', '_original_data']

    def __init__(self, uuid=None, device_id=None, device_manufacturer=None, device_platform=None, device_brand=None, device_type=None, app_version=None, os_version=None, os_lang=None, channel=None, resolution=None, original_data=None):
        self.uuid = uuid
        self.device_id = device_id
        self.device_manufacturer = device_manufacturer
        self.device_platform = device_platform
        self.device_brand = device_brand
        self.device_type = device_type
        self.app_version = app_version
        self.os_version = os_version
        self.os_lang = os_lang
        self.channel = channel
        self.resolution = resolution
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class DataDeviceInfoSchema(marshmallow.Schema):
    uuid = marshmallow.fields.String()  # 第一次安装启动时，有APP产生，见通用参数
    device_id = marshmallow.fields.String()  # 安卓 imei 值 / ios idfa 值example: 626363D0-90D4-06BF-C281-384E4E69D3E2
    device_manufacturer = marshmallow.fields.String()  # 手机生成厂商example: apple
    device_platform = marshmallow.fields.String()  # android or iphoneexample: android
    device_brand = marshmallow.fields.String()  # 手机品牌 huawei xiaomi ……example: Apple
    device_type = marshmallow.fields.String()  # 型号 FRD-AL00example: FRD-AL00
    app_version = marshmallow.fields.String()  # app版本号example: moremom1.1.2
    os_version = marshmallow.fields.String()  # 设备安卓或ios系统版本号 7.0 / 11.2.5example: 7.0
    os_lang = marshmallow.fields.String()  # 手机语言系统example: cn
    channel = marshmallow.fields.String()  # APP下载渠道example: xiaomi /  huawei / appstore 等
    resolution = marshmallow.fields.String()  # 设备分辨率example: 1024x768

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = DataDeviceInfo(**data)
        return obj


class DataMessage(object):
    __slots__ = ['id', 'from_user_id', 'status', 'subject', 'content', 'create_ts', 'to_user_id', '_original_data']

    def __init__(self, id, from_user_id, content, to_user_id, status=None, subject=None, create_ts=None, original_data=None):
        self.id = id
        self.from_user_id = from_user_id
        self.status = status
        self.subject = subject
        self.content = content
        self.create_ts = create_ts
        self.to_user_id = to_user_id
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class DataMessageSchema(marshmallow.Schema):
    id = marshmallow.fields.String(required=True, validate=validator.v_enc_message_id)
    from_user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_user_id)
    status = marshmallow.fields.String()
    subject = marshmallow.fields.String()
    content = marshmallow.fields.String(required=True)
    create_ts = marshmallow.fields.Integer()
    to_user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_user_id)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = DataMessage(**data)
        return obj


class DataPointDeposit(object):
    __slots__ = ['user_id', 'point', 'status', 'trade_no', 'transaction_id', 'payment_type', 'paied_ts', '_original_data']

    def __init__(self, user_id, point, status=None, trade_no=None, transaction_id=None, payment_type=None, paied_ts=None, original_data=None):
        self.user_id = user_id
        self.point = point
        self.status = status
        self.trade_no = trade_no
        self.transaction_id = transaction_id
        self.payment_type = payment_type
        self.paied_ts = paied_ts
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class DataPointDepositSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_user_id)
    point = marshmallow.fields.Decimal(required=True)
    status = marshmallow.fields.String()
    trade_no = marshmallow.fields.String()
    transaction_id = marshmallow.fields.String()
    payment_type = marshmallow.fields.String()
    paied_ts = marshmallow.fields.Integer()

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = DataPointDeposit(**data)
        return obj


class DataPointGrant(object):
    __slots__ = ['user_id', 'point', 'status', 'type', 'create_ts', '_original_data']

    def __init__(self, user_id, point, status=None, type=None, create_ts=None, original_data=None):
        self.user_id = user_id
        self.point = point
        self.status = status
        self.type = type
        self.create_ts = create_ts
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class DataPointGrantSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_user_id)
    point = marshmallow.fields.Decimal(required=True)
    status = marshmallow.fields.String()
    type = marshmallow.fields.String()
    create_ts = marshmallow.fields.Integer()

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = DataPointGrant(**data)
        return obj


class DataPointTX(object):
    __slots__ = ['from_user_id', 'to_user_id', 'point', 'status', 'type', 'create_ts', '_original_data']

    def __init__(self, from_user_id, to_user_id, point, status=None, type=None, create_ts=None, original_data=None):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.point = point
        self.status = status
        self.type = type
        self.create_ts = create_ts
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class DataPointTXSchema(marshmallow.Schema):
    from_user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_user_id)
    to_user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_user_id)
    point = marshmallow.fields.Decimal(required=True)
    status = marshmallow.fields.String()
    type = marshmallow.fields.String()
    create_ts = marshmallow.fields.Integer()

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = DataPointTX(**data)
        return obj


class DataPointWithdraw(object):
    __slots__ = ['user_id', 'point', 'status', 'payment_trade_no', 'payment_type', 'paied_ts', 'account_no', 'account_name', 'account_bank', 'create_ts', '_original_data']

    def __init__(self, user_id, point, status=None, payment_trade_no=None, payment_type=None, paied_ts=None, account_no=None, account_name=None, account_bank=None, create_ts=None, original_data=None):
        self.user_id = user_id
        self.point = point
        self.status = status
        self.payment_trade_no = payment_trade_no
        self.payment_type = payment_type
        self.paied_ts = paied_ts
        self.account_no = account_no
        self.account_name = account_name
        self.account_bank = account_bank
        self.create_ts = create_ts
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class DataPointWithdrawSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_user_id)
    point = marshmallow.fields.Decimal(required=True)
    status = marshmallow.fields.String()
    payment_trade_no = marshmallow.fields.String()
    payment_type = marshmallow.fields.String()
    paied_ts = marshmallow.fields.Integer()
    account_no = marshmallow.fields.String()
    account_name = marshmallow.fields.String()
    account_bank = marshmallow.fields.String()
    create_ts = marshmallow.fields.Integer()

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = DataPointWithdraw(**data)
        return obj


class DataUserPoint(object):
    __slots__ = ['user_id', 'point', 'total_grant', 'total_deposit', 'total_withdraw', '_original_data']

    def __init__(self, user_id, point, total_grant, total_deposit, total_withdraw, original_data=None):
        self.user_id = user_id
        self.point = point
        self.total_grant = total_grant
        self.total_deposit = total_deposit
        self.total_withdraw = total_withdraw
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class DataUserPointSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_user_id)
    point = marshmallow.fields.Integer(required=True)
    total_grant = marshmallow.fields.Integer(required=True)
    total_deposit = marshmallow.fields.Integer(required=True)
    total_withdraw = marshmallow.fields.Integer(required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = DataUserPoint(**data)
        return obj


class OSSDownloadURLResponseData(object):
    __slots__ = ['url', '_original_data']

    def __init__(self, url=None, original_data=None):
        self.url = url
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OSSDownloadURLResponseDataSchema(marshmallow.Schema):
    url = marshmallow.fields.URL(relative=True)  # 加密后的 URLexample: image

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OSSDownloadURLResponseData(**data)
        return obj


class ObjectInfo(object):
    __slots__ = ['key', 'mime_type', 'etag', 'size', 'persistent_id', 'width', 'height', 'duration', '_original_data']

    def __init__(self, key, etag, mime_type=None, size=None, persistent_id=None, width=None, height=None, duration=None, original_data=None):
        self.key = key
        self.mime_type = mime_type
        self.etag = etag
        self.size = size
        self.persistent_id = persistent_id
        self.width = width
        self.height = height
        self.duration = duration
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ObjectInfoSchema(marshmallow.Schema):
    key = marshmallow.fields.String(required=True)  # oss keyexample: user_id_123/avatar/2018/03/138/etag.jpg
    mime_type = marshmallow.fields.String()  # 文件类型 mimeTypeexample: image/jpeg
    etag = marshmallow.fields.String(required=True)  # 使用 qiniu sdk 计算的 etagexample: 7DsdkdFSKkdljfksQWET-TUI
    size = marshmallow.fields.Integer()  # 文件大小example: 536123
    persistent_id = marshmallow.fields.String()  # 七牛持久化操作 ID 用于查询视频转码和截图等异步操作的结果example: z1.5ade998d856db843bc8fe6f2
    width = marshmallow.fields.Integer()  # 分辨率 宽example: 1080
    height = marshmallow.fields.Integer()  # 分辨率 高example: 1920
    duration = marshmallow.fields.Integer()  # 播放时长(秒)example: 30

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ObjectInfo(**data)
        return obj


class OrderCancelResponse_Data(object):
    __slots__ = ['order_id', '_original_data']

    def __init__(self, order_id=None, original_data=None):
        self.order_id = order_id
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderCancelResponse_DataSchema(marshmallow.Schema):
    order_id = marshmallow.fields.String(validate=validator.v_enc_id)  # 取消订单 idexample: uuid_order_1

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderCancelResponse_Data(**data)
        return obj


class OrderPayResponse_Data(object):
    __slots__ = ['order_ids', 'paid', 'balance', '_original_data']

    def __init__(self, order_ids=None, paid=None, balance=None, original_data=None):
        self.order_ids = order_ids
        self.paid = paid
        self.balance = balance
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderPayResponse_DataSchema(marshmallow.Schema):
    order_ids = marshmallow.fields.List(marshmallow.fields.String(validate=validator.v_enc_id))
    paid = marshmallow.fields.Integer()  # 支付金额(摩尔豆)example: 220
    balance = marshmallow.fields.Integer()  # 账户余额(摩尔豆)example: 1800

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderPayResponse_Data(**data)
        return obj


class OrderSubmitRequest_Children(object):
    __slots__ = ['name', 'gender', '_original_data']

    def __init__(self, name, gender, original_data=None):
        self.name = name
        self.gender = gender
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderSubmitRequest_ChildrenSchema(marshmallow.Schema):
    name = marshmallow.fields.String(required=True)  # example: 刘小力
    gender = marshmallow.fields.String(required=True)  # example: 女

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderSubmitRequest_Children(**data)
        return obj


class OrderSubmitResponse_Data(object):
    __slots__ = ['order_ids', 'reserved_time', 'balance', 'diff', '_original_data']

    def __init__(self, order_ids=None, reserved_time=None, balance=None, diff=None, original_data=None):
        self.order_ids = order_ids
        self.reserved_time = reserved_time
        self.balance = balance
        self.diff = diff
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderSubmitResponse_DataSchema(marshmallow.Schema):
    order_ids = marshmallow.fields.List(marshmallow.fields.String(validate=validator.v_enc_id))
    reserved_time = marshmallow.fields.Integer()  # 未支付状态下 订单保留时间(秒)example: 2700
    balance = marshmallow.fields.Integer()  # 账户余额(摩尔豆)example: 50
    diff = marshmallow.fields.Integer()  # 若账户余额不够支付本订单 该值为差额: 订单价格 - 账户余额 (摩尔豆)example: 150

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderSubmitResponse_Data(**data)
        return obj


class ShareActivityPublishRequest(object):
    __slots__ = ['start_ts', 'end_ts', 'price', 'tags', 'description', 'accompanied', '_original_data']

    def __init__(self, start_ts=None, end_ts=None, price=None, tags=None, description=None, accompanied=None, original_data=None):
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.price = price
        self.tags = tags
        self.description = description
        self.accompanied = accompanied
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ShareActivityPublishRequestSchema(marshmallow.Schema):
    start_ts = marshmallow.fields.Integer()  # 几点开始接待孩子 时间戳example: 1524644418
    end_ts = marshmallow.fields.Integer()  # 几点结束 时间戳example: 1524644418
    price = marshmallow.fields.Integer()  # 价格(摩尔豆)example: 60
    tags = marshmallow.fields.List(marshmallow.fields.Integer())  # 活动内容标签 IDexample: [2, 3, 4]
    description = marshmallow.fields.String()  # 补充描述example: 请出入想补充的信息 我想和孩子一起玩玩
    accompanied = marshmallow.fields.Boolean(missing=True)  # 是否必须家长陪同example: True

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ShareActivityPublishRequest(**data)
        return obj


class ShareActivityPublishResponseData(object):
    __slots__ = ['id', '_original_data']

    def __init__(self, id, original_data=None):
        self.id = id
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ShareActivityPublishResponseDataSchema(marshmallow.Schema):
    id = marshmallow.fields.String(required=True, validate=validator.v_enc_id)  # 本次发布的活动 IDexample: 123

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ShareActivityPublishResponseData(**data)
        return obj


class ShareActivityTagsResponseItem(object):
    __slots__ = ['id', 'text', '_original_data']

    def __init__(self, id, text, original_data=None):
        self.id = id
        self.text = text
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ShareActivityTagsResponseItemSchema(marshmallow.Schema):
    id = marshmallow.fields.Integer(required=True)  # 标签 IDexample: 3
    text = marshmallow.fields.String(required=True)  # 标签文字example: 唱歌

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ShareActivityTagsResponseItem(**data)
        return obj


class Status(object):
    __slots__ = ['code', 'msg', '_original_data']

    def __init__(self, code, msg, original_data=None):
        self.code = code
        self.msg = msg
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class StatusSchema(marshmallow.Schema):
    code = marshmallow.fields.Integer(required=True)  # 错误码，成功为 0
    msg = marshmallow.fields.String(required=True)  # 错误信息

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = Status(**data)
        return obj


class UploadTokenResponseData(object):
    __slots__ = ['token', 'expiration', '_original_data']

    def __init__(self, token=None, expiration=None, original_data=None):
        self.token = token
        self.expiration = expiration
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UploadTokenResponseDataSchema(marshmallow.Schema):
    token = marshmallow.fields.String()  # 上传tokenexample: EWEEKOOgH774kafCEiLp7dMwQmQ7aqmnTFTlJXzf:yIeNbSmjYbeENyi3ZIj
    expiration = marshmallow.fields.String()  # token过期时间(UTC)example: 2018-03-26 04:31:24

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UploadTokenResponseData(**data)
        return obj


class UserChildDeleteRequest(object):
    __slots__ = ['id', '_original_data']

    def __init__(self, id, original_data=None):
        self.id = id
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserChildDeleteRequestSchema(marshmallow.Schema):
    id = marshmallow.fields.String(required=True)  # 孩子 idexample: 123

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserChildDeleteRequest(**data)
        return obj


class UserChildUpdateData(object):
    __slots__ = ['id', 'uuid', 'nickname', 'realname', 'id_card_no', '_original_data']

    def __init__(self, id=None, uuid=None, nickname=None, realname=None, id_card_no=None, original_data=None):
        self.id = id
        self.uuid = uuid
        self.nickname = nickname
        self.realname = realname
        self.id_card_no = id_card_no
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserChildUpdateDataSchema(marshmallow.Schema):
    id = marshmallow.fields.Integer()  # 孩子 idexample: 112
    uuid = marshmallow.fields.String(validate=validator.v_enc_id)  # example: uuid_child_1
    nickname = marshmallow.fields.String()  # 昵称example: powerfulio
    realname = marshmallow.fields.String()  # 真实姓名example: 刘小力
    id_card_no = marshmallow.fields.String(validate=validator.v_id_number)  # 身份证号example: 220***********2318

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserChildUpdateData(**data)
        return obj


class UserFavor(object):
    __slots__ = ['op_type', 'to_user_id', 'relation_type', '_original_data']

    def __init__(self, op_type, to_user_id, relation_type, original_data=None):
        self.op_type = op_type
        self.to_user_id = to_user_id
        self.relation_type = relation_type
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserFavorSchema(marshmallow.Schema):
    op_type = marshmallow.fields.Integer(required=True)  # 操作类型
    to_user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_id)  # 关系用户user_id
    relation_type = marshmallow.fields.String(required=True)  # favor类型example: like

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserFavor(**data)
        return obj


class UserIdentifyLivenessResponseData(object):
    __slots__ = ['result', '_original_data']

    def __init__(self, result=None, original_data=None):
        self.result = result
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserIdentifyLivenessResponseDataSchema(marshmallow.Schema):
    result = marshmallow.fields.Integer()  # 检测是否通过example: 1

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserIdentifyLivenessResponseData(**data)
        return obj


class UserInfo(object):
    __slots__ = ['nickname', 'realname', 'mobile', 'id_card_no', 'child_relation', 'degree', 'avatar_url', '_original_data']

    def __init__(self, nickname=None, realname=None, mobile=None, id_card_no=None, child_relation=None, degree=None, avatar_url=None, original_data=None):
        self.nickname = nickname
        self.realname = realname
        self.mobile = mobile
        self.id_card_no = id_card_no
        self.child_relation = child_relation
        self.degree = degree
        self.avatar_url = avatar_url
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserInfoSchema(marshmallow.Schema):
    nickname = marshmallow.fields.String()  # 昵称example: 刘小力的妈妈
    realname = marshmallow.fields.String()  # 真实姓名example: 刘大力
    mobile = marshmallow.fields.String(validate=validator.v_mobile)  # 手机号example: 13618810002
    id_card_no = marshmallow.fields.String(validate=validator.v_id_number)  # 身份证号example: 220***********2318
    child_relation = marshmallow.fields.String()  # 和孩子的关系example: 妈妈
    degree = marshmallow.fields.String()  # 最高学历example: 博士
    avatar_url = marshmallow.fields.URL(relative=True)  # 个人头像图片 URLexample: qiniu.com/image/2018/03/11/avatar.jpg

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserInfo(**data)
        return obj


class UserInfoUpdateResponseData(object):
    __slots__ = ['id', '_original_data']

    def __init__(self, id, original_data=None):
        self.id = id
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserInfoUpdateResponseDataSchema(marshmallow.Schema):
    id = marshmallow.fields.String(required=True, validate=validator.v_enc_id)  # example: uuid_user_1

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserInfoUpdateResponseData(**data)
        return obj


class UserUploadDoneRequest(object):
    __slots__ = ['cloud', 'category', 'key', 'etag', 'persistentId', 'mimeType', 'size', 'reftag', '_original_data']

    def __init__(self, cloud, category, key, etag, persistentId=None, mimeType=None, size=None, reftag=None, original_data=None):
        self.cloud = cloud
        self.category = category
        self.key = key
        self.etag = etag
        self.persistentId = persistentId
        self.mimeType = mimeType
        self.size = size
        self.reftag = reftag
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserUploadDoneRequestSchema(marshmallow.Schema):
    cloud = marshmallow.fields.String(required=True)  # 云服务(qiniu)example: qiniu
    category = marshmallow.fields.String(required=True)  # 应用层 categoryexample: video
    key = marshmallow.fields.String(required=True)  # oss keyexample: user_id_123/avatar/2018/03/138/etag.jpg
    etag = marshmallow.fields.String(required=True)  # 使用 qiniu sdk 计算的 etagexample: 7DsdkdFSKkdljfksQWET-TUI
    persistentId = marshmallow.fields.String()  # 七牛上传文件成功后返回的 persistentIdexample: z1.5ad99a2b856db843bcfff1de
    mimeType = marshmallow.fields.String()  # 文件类型 mimeTypeexample: image/jpeg
    size = marshmallow.fields.Integer()  # 文件大小example: 536123
    reftag = marshmallow.fields.String()  # 引用tag 表示该文件的使用方式 如: avatar、intro-videoexample: intro-video

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserUploadDoneRequest(**data)
        return obj


class UserUploadDoneResponseData(object):
    __slots__ = ['id', '_original_data']

    def __init__(self, id, original_data=None):
        self.id = id
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserUploadDoneResponseDataSchema(marshmallow.Schema):
    id = marshmallow.fields.String(required=True, validate=validator.v_enc_id)  # 文件 IDexample: 123

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserUploadDoneResponseData(**data)
        return obj


class UserVideo(object):
    __slots__ = ['cover_url', 'video_url', 'size', 'duration', 'width', 'height', '_original_data']

    def __init__(self, cover_url=None, video_url=None, size=None, duration=None, width=None, height=None, original_data=None):
        self.cover_url = cover_url
        self.video_url = video_url
        self.size = size
        self.duration = duration
        self.width = width
        self.height = height
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserVideoSchema(marshmallow.Schema):
    cover_url = marshmallow.fields.URL(relative=True)  # 视频快照截图 URLexample: http://p5zmpa3g9.bkt.clouddn.com/cover.jpg
    video_url = marshmallow.fields.URL(relative=True)  # 视频URLexample: http://p5zmpa3g9.bkt.clouddn.com/video.mp4
    size = marshmallow.fields.Integer()  # 视频文件大小(字节)example: 10240002
    duration = marshmallow.fields.Integer()  # 视频播放时长(秒)example: 30
    width = marshmallow.fields.Integer()  # 视频分辨率 宽example: 800
    height = marshmallow.fields.Integer()  # 视频分辨率 高example: 600

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserVideo(**data)
        return obj


class AuthMobileCodeResponseData(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data=None, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class AuthMobileCodeResponseDataSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.Nested(AuthMobileCodeResponseData_DataSchema())

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = AuthMobileCodeResponseData(**data)
        return obj


class AuthMobileLoginRequest(object):
    __slots__ = ['mobile', 'password', 'child_info', '_original_data']

    def __init__(self, mobile, password, child_info=None, original_data=None):
        self.mobile = mobile
        self.password = password
        self.child_info = child_info
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class AuthMobileLoginRequestSchema(marshmallow.Schema):
    mobile = marshmallow.fields.String(required=True, validate=validator.v_mobile)  # 明文手机号
    password = marshmallow.fields.String(required=True, validate=marshmallow.validate.Length(min=4, max=4))  # 登录时发送的验证码
    child_info = marshmallow.fields.Nested(AuthMobileLoginRequest_ChildInfoSchema())

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = AuthMobileLoginRequest(**data)
        return obj


class CarerApplyRequestData_Video(object):
    __slots__ = ['intro', 'playground', 'extra', '_original_data']

    def __init__(self, intro=None, playground=None, extra=None, original_data=None):
        self.intro = intro
        self.playground = playground
        self.extra = extra
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class CarerApplyRequestData_VideoSchema(marshmallow.Schema):
    intro = marshmallow.fields.Nested(ObjectInfoSchema())
    playground = marshmallow.fields.Nested(ObjectInfoSchema())
    extra = marshmallow.fields.List(marshmallow.fields.Nested(ObjectInfoSchema()))

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = CarerApplyRequestData_Video(**data)
        return obj


class CarerInfoGetResponseData(object):
    __slots__ = ['nickname', 'identified', 'degree', 'care_exp', 'child_age_min', 'child_age_max', 'avatar_url', 'address', 'distance', 'liked', 'like_count', 'followed', 'follow_count', 'videos', '_original_data']

    def __init__(self, nickname=None, identified=None, degree=None, care_exp=None, child_age_min=None, child_age_max=None, avatar_url=None, address=None, distance=None, liked=None, like_count=None, followed=None, follow_count=None, videos=None, original_data=None):
        self.nickname = nickname
        self.identified = identified
        self.degree = degree
        self.care_exp = care_exp
        self.child_age_min = child_age_min
        self.child_age_max = child_age_max
        self.avatar_url = avatar_url
        self.address = address
        self.distance = distance
        self.liked = liked
        self.like_count = like_count
        self.followed = followed
        self.follow_count = follow_count
        self.videos = videos
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class CarerInfoGetResponseDataSchema(marshmallow.Schema):
    nickname = marshmallow.fields.String()  # 昵称example: 小番茄的妈妈
    identified = marshmallow.fields.Boolean()  # 是否实名认证example: True
    degree = marshmallow.fields.String()  # 学历example: 硕士
    care_exp = marshmallow.fields.Integer()  # 带娃经验(年)example: 5
    child_age_min = marshmallow.fields.Integer()  # 接待孩子最小年龄
    child_age_max = marshmallow.fields.Integer()  # 接待孩子最大年龄example: 6
    avatar_url = marshmallow.fields.URL(relative=True)  # 头像图片 URLexample: qiniu.com/image/2018/03/11/avatar.jpg
    address = marshmallow.fields.Nested(AddressSchema())
    distance = marshmallow.fields.String()  # 与用户的距离example: 3.1km(>=1000米) 128m(<1000m)
    liked = marshmallow.fields.Boolean()  # 是否赞过
    like_count = marshmallow.fields.Integer()  # 点赞次数example: 100
    followed = marshmallow.fields.Boolean()  # 是否已关注
    follow_count = marshmallow.fields.Integer()  # 关注人数example: 28
    videos = marshmallow.fields.List(marshmallow.fields.Nested(UserVideoSchema()))  # 看护人的视频

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = CarerInfoGetResponseData(**data)
        return obj


class FavorModifyResponse(object):
    __slots__ = ['status', '_original_data']

    def __init__(self, status, original_data=None):
        self.status = status
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class FavorModifyResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = FavorModifyResponse(**data)
        return obj


class MessageListResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data=None, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class MessageListResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.List(marshmallow.fields.Nested(DataMessageSchema()))

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = MessageListResponse(**data)
        return obj


class MessageResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data=None, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class MessageResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.Nested(DataMessageSchema())

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = MessageResponse(**data)
        return obj


class OrderCancelResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderCancelResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.Nested(OrderCancelResponse_DataSchema(), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderCancelResponse(**data)
        return obj


class OrderPayResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderPayResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.Nested(OrderPayResponse_DataSchema(), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderPayResponse(**data)
        return obj


class OrderSubmitRequest(object):
    __slots__ = ['user_id', 'item_ids', 'children', 'insurer_name', 'insured_name', 'remark', '_original_data']

    def __init__(self, user_id, item_ids, children, insurer_name, insured_name, remark=None, original_data=None):
        self.user_id = user_id
        self.item_ids = item_ids
        self.children = children
        self.insurer_name = insurer_name
        self.insured_name = insured_name
        self.remark = remark
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderSubmitRequestSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_id)  # example: uuid_user_1
    item_ids = marshmallow.fields.List(marshmallow.fields.String(validate=validator.v_enc_id), required=True)
    children = marshmallow.fields.List(marshmallow.fields.Nested(OrderSubmitRequest_ChildrenSchema()), required=True)
    insurer_name = marshmallow.fields.String(required=True)  # example: 刘大力
    insured_name = marshmallow.fields.String(required=True)  # example: 刘小力
    remark = marshmallow.fields.String()  # example: 宝宝很聪明, 请多关照!

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderSubmitRequest(**data)
        return obj


class OrderSubmitResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderSubmitResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.Nested(OrderSubmitResponse_DataSchema(), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderSubmitResponse(**data)
        return obj


class PointDepositListResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data=None, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class PointDepositListResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.List(marshmallow.fields.Nested(DataPointDepositSchema()))

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = PointDepositListResponse(**data)
        return obj


class PointGrantListResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data=None, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class PointGrantListResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.List(marshmallow.fields.Nested(DataPointGrantSchema()))

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = PointGrantListResponse(**data)
        return obj


class PointTXListResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data=None, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class PointTXListResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.List(marshmallow.fields.Nested(DataPointTXSchema()))

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = PointTXListResponse(**data)
        return obj


class PointWithdrawListResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data=None, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class PointWithdrawListResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.List(marshmallow.fields.Nested(DataPointWithdrawSchema()))

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = PointWithdrawListResponse(**data)
        return obj


class RecommendCarerResponseDataItem(object):
    __slots__ = ['user_id', 'nickname', 'avatar_url', 'address', 'distance', 'liked', 'like_count', 'followed', 'follow_count', 'videos', '_original_data']

    def __init__(self, user_id=None, nickname=None, avatar_url=None, address=None, distance=None, liked=None, like_count=None, followed=None, follow_count=None, videos=None, original_data=None):
        self.user_id = user_id
        self.nickname = nickname
        self.avatar_url = avatar_url
        self.address = address
        self.distance = distance
        self.liked = liked
        self.like_count = like_count
        self.followed = followed
        self.follow_count = follow_count
        self.videos = videos
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class RecommendCarerResponseDataItemSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(validate=validator.v_enc_id)  # 用户 idexample: 123456
    nickname = marshmallow.fields.String()  # 昵称example: xxx的妈妈
    avatar_url = marshmallow.fields.URL(relative=True)  # 头像图片 URLexample: qiniu.com/image/2018/03/11/avatar.jpg
    address = marshmallow.fields.String()  # 简短地址
    distance = marshmallow.fields.String()  # 距离example: 1.2km(821m)
    liked = marshmallow.fields.Boolean()  # 是否赞过example: True
    like_count = marshmallow.fields.Integer()  # 被点赞次数example: 100
    followed = marshmallow.fields.Boolean()  # 是否收藏过
    follow_count = marshmallow.fields.Integer()  # 被收藏次数example: 28
    videos = marshmallow.fields.List(marshmallow.fields.Nested(UserVideoSchema()))  # 看护人的视频

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = RecommendCarerResponseDataItem(**data)
        return obj


class ServiceItem(object):
    __slots__ = ['user_id', 'provider_name', 'start_ts', 'end_ts', 'child_count', 'child_limit', 'price', 'description', 'address', '_original_data']

    def __init__(self, user_id, provider_name, start_ts, end_ts, child_limit, price, description, child_count=None, address=None, original_data=None):
        self.user_id = user_id
        self.provider_name = provider_name
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.child_count = child_count
        self.child_limit = child_limit
        self.price = price
        self.description = description
        self.address = address
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ServiceItemSchema(marshmallow.Schema):
    user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_id)  # 服务提供者 idexample: uuid_user_123
    provider_name = marshmallow.fields.String(required=True)  # 服务提供者的显示名example: 小番茄的妈妈
    start_ts = marshmallow.fields.Integer(required=True)  # 开始时间example: 1521550268000
    end_ts = marshmallow.fields.Integer(required=True)  # 结束时间example: 1521553868000
    child_count = marshmallow.fields.Integer()  # 已报名孩子人数example: 8
    child_limit = marshmallow.fields.Integer(required=True)  # 可报名孩子总数example: 20
    price = marshmallow.fields.Integer(required=True)  # 价格 摩尔币example: 160
    description = marshmallow.fields.String(required=True)  # 服务简介example: 这次要在开放的室内和宝宝们分享故事绘本
    address = marshmallow.fields.Nested(AddressSchema())

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ServiceItem(**data)
        return obj


class StatusResponse(object):
    __slots__ = ['status', '_original_data']

    def __init__(self, status, original_data=None):
        self.status = status
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class StatusResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = StatusResponse(**data)
        return obj


class UserIdentifyLivenessRequest(object):
    __slots__ = ['realname', 'idcard_no', 'liveness_id', 'idcard_image', 'live_image', 'info', '_original_data']

    def __init__(self, realname, idcard_no, liveness_id, idcard_image=None, live_image=None, info=None, original_data=None):
        self.realname = realname
        self.idcard_no = idcard_no
        self.liveness_id = liveness_id
        self.idcard_image = idcard_image
        self.live_image = live_image
        self.info = info
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserIdentifyLivenessRequestSchema(marshmallow.Schema):
    realname = marshmallow.fields.String(required=True)  # 真实姓名example: 刘大力
    idcard_no = marshmallow.fields.String(required=True)  # 身份证号example: 220326199308125277
    liveness_id = marshmallow.fields.String(required=True)  # 活体检测 IDexample: 86be940bea6c4b35a2e0e9829b20d51d
    idcard_image = marshmallow.fields.Nested(ObjectInfoSchema())
    live_image = marshmallow.fields.Nested(ObjectInfoSchema())
    info = marshmallow.fields.String()  # 其他有用信息 格式化成 json 串

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserIdentifyLivenessRequest(**data)
        return obj


class UserInfoUpdateRequest(object):
    __slots__ = ['realname', 'mobile', 'id_card_no', 'child_relation', 'degree', 'avatar', '_original_data']

    def __init__(self, realname=None, mobile=None, id_card_no=None, child_relation=None, degree=None, avatar=None, original_data=None):
        self.realname = realname
        self.mobile = mobile
        self.id_card_no = id_card_no
        self.child_relation = child_relation
        self.degree = degree
        self.avatar = avatar
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserInfoUpdateRequestSchema(marshmallow.Schema):
    realname = marshmallow.fields.String()  # 真实姓名example: 刘大力
    mobile = marshmallow.fields.String(validate=validator.v_mobile)  # 手机号example: 13618810002
    id_card_no = marshmallow.fields.String(validate=validator.v_id_number)  # 身份证号example: 220324199608192318
    child_relation = marshmallow.fields.Integer()  # 和孩子的关系example: 1
    degree = marshmallow.fields.Integer()  # 最高学历example: 1
    avatar = marshmallow.fields.Nested(ObjectInfoSchema())

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserInfoUpdateRequest(**data)
        return obj


class UserPointResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data=None, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class UserPointResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.Nested(DataUserPointSchema())

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = UserPointResponse(**data)
        return obj


class CarerApplyRequestData(object):
    __slots__ = ['video', 'degree', 'address', 'child_count', 'child_age_min', 'child_age_max', 'identify_result', 'birth_certificate', '_original_data']

    def __init__(self, video, degree, address, birth_certificate, child_count=None, child_age_min=None, child_age_max=None, identify_result=None, original_data=None):
        self.video = video
        self.degree = degree
        self.address = address
        self.child_count = child_count
        self.child_age_min = child_age_min
        self.child_age_max = child_age_max
        self.identify_result = identify_result
        self.birth_certificate = birth_certificate
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class CarerApplyRequestDataSchema(marshmallow.Schema):
    video = marshmallow.fields.Nested(CarerApplyRequestData_VideoSchema(), required=True)
    degree = marshmallow.fields.Integer(required=True)  # 最高学历example: 1
    address = marshmallow.fields.Nested(AddressSchema(), required=True)
    child_count = marshmallow.fields.Integer()  # 接待孩子数example: 10
    child_age_min = marshmallow.fields.Integer()  # 接待孩子最小年龄example: 1
    child_age_max = marshmallow.fields.Integer()  # 接待孩子最大年龄example: 6
    identify_result = marshmallow.fields.Boolean()  # 实名认证结果example: True
    birth_certificate = marshmallow.fields.Nested(ObjectInfoSchema(), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = CarerApplyRequestData(**data)
        return obj


class ServiceOrder(object):
    __slots__ = ['id', 'user_id', 'status', 'create_ts', 'children', 'insurer_name', 'insurer_id', 'insured_name', 'insured_id', 'insurance_id', 'insurance_summary', 'remark', 'item', '_original_data']

    def __init__(self, user_id, item, id=None, status=None, create_ts=None, children=None, insurer_name=None, insurer_id=None, insured_name=None, insured_id=None, insurance_id=None, insurance_summary=None, remark=None, original_data=None):
        self.id = id
        self.user_id = user_id
        self.status = status
        self.create_ts = create_ts
        self.children = children
        self.insurer_name = insurer_name
        self.insurer_id = insurer_id
        self.insured_name = insured_name
        self.insured_id = insured_id
        self.insurance_id = insurance_id
        self.insurance_summary = insurance_summary
        self.remark = remark
        self.item = item
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class ServiceOrderSchema(marshmallow.Schema):
    id = marshmallow.fields.String(validate=validator.v_enc_id)  # example: uuid_order_1
    user_id = marshmallow.fields.String(required=True, validate=validator.v_enc_id)  # example: uuid_user_1
    status = marshmallow.fields.String()  # 订单状态
    create_ts = marshmallow.fields.Integer()  # example: 1521550268
    children = marshmallow.fields.List(marshmallow.fields.Nested(ChildSchema()))
    insurer_name = marshmallow.fields.String()  # example: 刘大力
    insurer_id = marshmallow.fields.String()  # example: 220326199308125277
    insured_name = marshmallow.fields.String()  # example: 刘小力
    insured_id = marshmallow.fields.String()  # example: 220324201503025266
    insurance_id = marshmallow.fields.String(validate=validator.v_enc_id)  # example: uuid_insurance_123
    insurance_summary = marshmallow.fields.String()  # example: 平台联合太平洋保险 为此单投保10万元
    remark = marshmallow.fields.String()  # example: 宝宝很聪明, 请多关照!
    item = marshmallow.fields.Nested(ServiceItemSchema(), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = ServiceOrder(**data)
        return obj


class OrderGetResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderGetResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.Nested(ServiceOrderSchema(), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderGetResponse(**data)
        return obj


class OrderListResponse(object):
    __slots__ = ['status', 'data', '_original_data']

    def __init__(self, status, data, original_data=None):
        self.status = status
        self.data = data
        self._original_data = original_data

    @property
    def dict(self):
        return self._original_data


class OrderListResponseSchema(marshmallow.Schema):
    status = marshmallow.fields.Nested(StatusSchema(), required=True)
    data = marshmallow.fields.List(marshmallow.fields.Nested(ServiceOrderSchema()), required=True)

    @marshmallow.post_load(pass_original=True)
    def make_object(self, data, original_data):
        data['original_data'] = original_data
        obj = OrderListResponse(**data)
        return obj
