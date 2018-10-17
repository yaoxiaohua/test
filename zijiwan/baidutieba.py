# coding: utf-8
import requests
# 定义变量
name = []
phone = []
weixin = []
zhiwu = []

company = []
F_leixing = []
F_diqu = []
F_time = []
F_guimo = []

# 登陆
s = requests.session()
url = 'http://www.bdwork.com//member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LGK1z&inajax=1'
header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 ',
            'Connection': 'keep-alive'
            }
body = {
    'formhash':'1f5c6580',
    'referer':'http://www.bdwork.com/',
    'username':'17621211515',
    'password':'147258369',
    'questionid':'0',
    'answer':''
}
login = s.post(url,headers=header,data=body)
cook = login.text
url2 = 'http://www.bdwork.com/serviceprovider/index'
index = s.get(url2,headers=header)
t = index.text
print(t)



