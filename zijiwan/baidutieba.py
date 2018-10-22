# coding: utf-8
import requests
from bs4 import BeautifulSoup

# 定义文件
bdwork = open('bdwork.txt', 'a')
# 定义变量
name = []
phone = []

company = []
F_xiangqing = []


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
n = 1
while n < 44:
    url2 = 'http://www.bdwork.com/member.php?mod=serviceprovider_list&page=%s'%n
    index = s.get(url2,headers=header)
    t = index.text
    soup = BeautifulSoup(t, 'lxml')
    # 详情页url
    #q用来控制url路径，从0开始
    q = 0
    # 此处要开始循环
    while q < 30:
        print('第%s页，第%s个'%(n,q+1))
        w = soup.select('a.pic')[q]
        url3 = 'http://www.bdwork.com'+w['href']
        print(url3)
        quzhi = s.get(url3,headers=header)
        y = quzhi.text
        soup1 = BeautifulSoup(y,'lxml')
        # w1包含了，名字和职务，w2包含了手机号，电话，微信，邮箱
        w1 = soup1.select('div.brand_contact i')
        w2 = soup1.select('div.brand_contact p')
        # w3是公司的基本信息，w4时服务商名称
        w3 = soup1.select('div.brand_info span')
        w4 = soup1.select('div.brand_info h1')
        # 定义一个变量，来控制w1w2的底标
        l = 0
        while l < len(w1):
            name.append(w1[l].get_text())
            bdwork.writelines([w1[l].get_text(),'\n'])
            print(w1[l].get_text(),'\n')
            l+=1
        r = 0
        while r < len(w2):
            phone.append(w2[r].get_text())
            bdwork.writelines([w2[r].get_text(),'\n'])
            print(w2[r].get_text(),'\n')
            r+=1
        d= 0
        while d < len(w3):
            company.append(w4[d].get_text())
            F_xiangqing.append(w3[d].get_text())
            print(w4[d].get_text(),'\n')
            print(w3[d].get_text(),'\n===================================================================================\n')
            bdwork.writelines([w4[d].get_text(),'\n'])
            bdwork.writelines([w3[d].get_text(),'\n===================================================================================\n'])
            d+=1
        q += 1
    n += 1
bdwork.close()



