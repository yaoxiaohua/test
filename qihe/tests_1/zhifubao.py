# coding:utf-8
import requests
from qihe.tests_1 import login
s = requests.session()
def test_z_1():
    '''
    支付宝刷新卡购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'1',
        'chargetype': '0',
        'transtype':'-22',
        'applyid':'1'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()
def test_z_2():
    '''
    支付宝千斤顶购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'0',
        'chargetype': '0',
        'transtype':'-17',
        'applyid':'29'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_z_3():
    '''
    支付宝变色卡购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'0',
        'chargetype': '0',
        'transtype':'-17',
        'applyid':'44'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_z_4():
    '''
    支付宝改名卡购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'0',
        'chargetype': '0',
        'transtype':'-17',
        'applyid':'50'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_z_5():
    '''
    支付宝查看卡购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'0',
        'chargetype': '0',
        'transtype':'-26',
        'applyid':'1'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_z_6():
    '''
    支付宝置顶卡购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'0',
        'chargetype': '0',
        'transtype':'-17',
        'applyid':'41'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_z_7():
    '''
    支付宝c超级会员购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'0',
        'chargetype': '0',
        'transtype':'-15',
        'extra':'3'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_z_8():
    '''
    支付宝会员购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'0',
        'chargetype': '0',
        'transtype':'-16',
        'extra':'3'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_z_9():
    '''
    支付宝渠道商会员购买
    :return:state=1正确
    '''
    url = 'http://crmtest.bdwork.com/appapi.php?mod=pay_getTradeNumber'
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
        'auth':login.Login(s),
        'uid': '314948',
        'tuid':'0',
        'chargetype': '0',
        'transtype':'-27',
        'extra':'3'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()
