import os

from utils.pwdb.construct import construct

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

LOG_PATH = "gt-server.log"
AUDIT_LOG_PATH = "audit.log"

# MySQL Connection Config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "test_huatai",
        "USER": "root",
        "PASSWORD": "Geetest123..",
        "HOST": "10.0.0.196",
        "PORT": 3306,
        # "OPTIONS": {"charset": "utf8mb4"},
    }
}

## demo config
CID = "0" * 32
CKEY = "1" * 32
API_SERVER = "http://10.0.0.159"

## STATIC Server
STATIC_SERVER = "http://10.0.0.153"
# 后台设置的图片路径，需要和nginx相关目录相同
SLIDE_SOURCE_PATH = "/www/assests/20/slide/source/"

# 配置用户是使用SFTP模式上传图片还是使用共享磁盘的方式
# 值为True时代表使用SFTP，为False时表示使用共享磁盘
SFTP_SAVE_UPLOAD_PIC = True
# 图片存储绝对路径
SLIDE_SOURCE_ABS_PATH = "/www/assests/20/slide/source/"
SLIDE_FULLBG_PATH = "/www/assests/20/slide/full/"
SLIDE_BG_PATH = "/www/assests/20/slide/bg/"
SLIDE_SLICE_PATH = "/www/assests/20/slide/slice/"
CLICK_FULLBG_PATH = "/www/assests/30/click/"

STATIC_SERVER_AUTH = [
    ("root", "123qwe", "10.0.0.153", 22)
]

# 配置redis数据库的模式(cluster, single)
REDIS_MODULE = "single"
## Redis Cluster
REDIS_CLUSTER = [
    {
        "host": "10.0.0.159",
        "port": 7000
    },
    {
        "host": "10.0.0.159",
        "port": 7001
    },
    {
        "host": "10.0.0.159",
        "port": 7002
    }

]
## Redis Single
REDIS_HOST = "192.168.1.145"
REDIS_PWD = ""

## CORS Header Config
CORS_ORIGIN_ALLOW_ALL = False

DEFAULT_VERIFY_TYPE = {
    "verify_type": "ai",
    "sub_type": "",
    "urgency": 0
}

CONFIG_VALUES = ["click", "slide"]

# IP statistics result key
YESTERDAY_TOP_10_IP = "yesterday:ip:top:10"
YESTERDAY_CID_COUNTRY = "yesterday:cid:country"

# passtime statistics hash key
MONTH_PASSTIME_STAT = "month:passtime:hashkey"

DEFAULT_PASSSWOR = "geetest123"
# KMS config
KMS_TTL = 10245
source = construct("kms.bin", KMS_TTL)
if not source:
    raise ValueError("kms file error, please provide correct kms file")
exec(source)
# 网关验证部分的配置

# 权限密码校验
PASSWORD = "123"

# 联通账号配置
CU_CONFIG = {
    "ios_id": "99166000000000000151",
    "ios_key": "04ba9cc619234b52",
    "android_id": "99166000000000000151",
    "android_key": "04ba9cc619234b52"
}

# 电信账号配置
CT_CONFIG = {
    "ios_id": "8025233202",
    "ios_key": "H5JhMrCn47N8Ppcq6dlPvAQTJdZGrs0C",
    "android_id": "8025233202",
    "android_key": "H5JhMrCn47N8Ppcq6dlPvAQTJdZGrs0C"
}

# 未开启数据流量
NO_DATA_TRAFFIC = ['-20200', '-20201', '-20202']
# 数据流量不支持
NOT_SUPPORT_DATA_TRAFFIC = ['-40204', '-40304', '-40305']
# 移动获取token失败
CM_TOKEN_FAIL = ['-40101']
# 联通获取token失败
CU_TOKEN_FAIL = ['-40201']
# 电信获取token失败
CT_TOKEN_FAIL = ['-40301', '-40302']

# 项目路径
ROOT_DIR = os.path.abspath(os.path.dirname(__name__))
DOWNLOAD_PATH = ROOT_DIR + "/static/files"
STATISTICS_REPORT_PATH = DOWNLOAD_PATH + "/statistics"
if not os.path.isdir(STATISTICS_REPORT_PATH):
    os.makedirs(STATISTICS_REPORT_PATH, exist_ok=True)

if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CORS_ORIGIN_ALLOW_ALL = True

# 默认永久的captcha账号，界面不可操作
DEFAULT_PERSISTENT_CAPTCHA_ID = ["0" * 32]
