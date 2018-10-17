# coding:utf-8

import re
import time
from decimal import *
def zhuanhuan(a):
    s=a.replace('=',"':'")
    d=s.replace('&',"',\n'")
    print("'",d,"'")
    print(type(d))
zhuanhuan(a=input())
str = "auth = 'a123b';"
print(re.findall("auth = \'(.+?)';",str))


# l = 'asd①②12345a①②aq8e9①②①①①①①'
# a=l.replace('①','*')
# b=a.replace('②','*')
# print(b)


