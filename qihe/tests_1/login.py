# coding:utf-8
import requests
import re
def Login(s):
    '''
    保持uid	314948的登陆状态
    :return:提取auth的值
    '''
    url = 'http://crmtest.bdwork.com/member.php?mod=logging&action=login&referer='
    h = {
        'Host': 'crmtest.bdwork.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4092.1 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://crmtest.bdwork.com/home.php?mod=spacecp&ac=look',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8'
        }
    cookie = {
        'brandclick':'brandclick',
        'KY1F_c7af_saltkey':'c32x3x6a',
        'KY1F_c7af_lastvisit':'1533198615',
        'KY1F_c7af_sendmail':'1',
        'KY1F_c7af_noticeTitle':'1',
        'UM_distinctid':'164f9f95c5830e-0679413bf11568-4c531929-100200-164f9f95c59474',
        'KY1F_c7af__refer':'%252Fhome.php%253Fmod%253Dspacecp%2526ac%253Dlook',
        'CNZZDATA1259972829':'1337227657-1530510545-%7C1533198970',
        'Hm_lvt_aabf378828361ace85e070bda547e0c2':'1532587790,1532703535,1532934413,1533188504',
        'Hm_lpvt_aabf378828361ace85e070bda547e0c2':'1533202228',
        'Hm_lvt_855f1a9b2df256430c5190b4c155e0be':'1532587790,1532703535,1532934413,1533188504',
        'Hm_lpvt_855f1a9b2df256430c5190b4c155e0be':'1533202229',
        'KY1F_c7af_lastact':'1533202227%09member.php%09logging',
        'encodemobile':'cP22pue9GTQnWMxgrOUowqIFOw',
        'name':'17621212121',
        'KY1F_c7af_ulastactivity':'e4df0yITlF8mbtqQE5dAg%2FzDeXDv%2B3mOev0miMuxK8fR%2FG2WwF%2Fc',
        'KY1F_c7af_sid':'m3ApNB',
        'KY1F_c7af_auth':'b61asNdM0xvEJX17xo6x8LhP3d7utK0DAWkXCm23DiIx262XHLcqgzsh4Qdm7jOjCwsiIOGy0LJFiYiTlfwI%2BcQqpng',
        'KY1F_c7af_lastcheckfeed':'314948%7C1533202227',
        'KY1F_c7af_checkfollow':'1',
        'KY1F_c7af_lip':'116.226.114.196%2C1533201831',
        'KY1F_c7af_security_cookiereport':'921azQNj36RYks%2BTjCXtqUSWvv9kMJQOPGbKe4zawKNQngh3mPI8'
        }
    d = s.get(url,headers=h,cookies=cookie)
    r = d.text
    # if '吕振华' in r:
    #     print('登陆成功,提取auth：',)
    # else:
    #     print('登录失败')
    auth0 = re.findall(r"auth = \"(.+?)\";",r)
    auth = ''.join(auth0)
    return auth
if __name__ in '__main__':
    s = requests.session()
    # print('\'',''.join(Login(s)),'\'')
    print(Login(s))

