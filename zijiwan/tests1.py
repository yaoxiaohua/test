# coding:utf-8
import requests
import json
import re

#定义一个内置浏览器
s = requests.session()
def zz(s):
    url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html'
    r = s.get(url)
    js1 = r.json()
    print(type(js1))
    #print(js1)
    #取出想要的值
    #q = (js1['data'][0]['context'])
    #print(q)
    s = re.findall('由 (.+?) 签收',(js1['data'][0]['context']))
    print(s)
    print(type(s))

