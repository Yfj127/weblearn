from urllib.parse import quote
from hashlib import md5
from http import client
import random
import json


appid = "个人id号"
password = "个人密码"
def get_sign(salt, qurey):  # 生成调用API的签名
    sign = appid + qurey + str(salt) + password
    m = md5()
    m.update(sign.encode('utf-8'))
    return m.hexdigest()

def trans(qurey, from_lang='zh', to_lang='en'):  # 实现翻译功能
    http_client = None
    salt = random.randint(12345, 67890)
    sign = get_sign(salt, qurey)
    myurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + quote(
        qurey) + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        http_client = client.HTTPConnection('api.fanyi.baidu.com')  # 连接API
        http_client.request('GET', myurl)  #发起请求
        response = http_client.getresponse()  #获取响应对象
        content = json.loads(response.read())  # 将调用API的返回结果转为字典
        return content['trans_result'][0]['dst']  # 返回翻译内容
    except Exception as e:
        return e
    finally:
        if http_client:
            http_client.close()