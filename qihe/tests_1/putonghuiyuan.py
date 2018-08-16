# coding:utf-8
import requests
from qihe.tests_1 import login
s = requests.session()
def test_g_7(auth):
    '''
    普通会员购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_transeMoney'
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://crmtest.bdwork.com/member.php?mod=txl&act=zhifu&zhifu_type=4&authorid=1&bump_id=1&id=33&idtype=tid&tid=&url=',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'name=17621212121',
        'Host': 'crmtest.bdwork.com',
        'Content-Length': '88'
        }

    body = {
        'auth': login.Login(s), 'uid': '314948', 'tuid': '0', 'amount': '1', 'transtype': '-16', 'extra': '3'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()
# if __name__ in '__main__':
#     auth = login.Login(s)
#     print(test_g_7(auth))