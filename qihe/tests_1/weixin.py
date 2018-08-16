# coding:utf-8
import requests
from qihe.tests_1 import login
s = requests.session()
def test_w_1():
    '''
    微信刷新卡购买
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
        'chargetype': '1',
        'transtype':'-22',
        'applyid':'1'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()
def test_w_2():
    '''
    微信千斤顶购买
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
        'chargetype': '1',
        'transtype':'-17',
        'applyid':'29'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_w_3():
    '''
    微信变色卡购买
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
        'chargetype': '1',
        'transtype':'-17',
        'applyid':'44'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_w_4():
    '''
    微信改名卡购买
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
        'chargetype': '1',
        'transtype':'-17',
        'applyid':'50'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_w_5():
    '''
    微信查看卡购买
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
        'chargetype': '1',
        'transtype':'-26',
        'applyid':'1'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_w_6():
    '''
    微信置顶卡购买
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
        'chargetype': '1',
        'transtype':'-17',
        'applyid':'41'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_w_7():
    '''
    微信c超级会员购买
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
        'chargetype': '1',
        'transtype':'-15',
        'extra':'3'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_w_8():
    '''
    微信会员购买
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
        'chargetype': '1',
        'transtype':'-16',
        'extra':'3'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()

def test_w_9():
    '''
    微信渠道商会员购买
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
        'chargetype': '1',
        'transtype':'-27',
        'extra':'3'
        }
    r = s.post(url,data=body,headers=h)
    return r.json()