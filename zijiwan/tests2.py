# coding:utf-8
import requests
import json
s = requests.session()

def add_cookies():
    r=requests.cookies.RequestsCookieJar()
    r.set('KY1F_c7af_saltkey','Xc2sS6La')
    r.set('KY1F_c7af_auth','6766Qc4dVEnum847vJ9i1dCqeUIkZSFUxq%2FpIyyWtnMzWYfxsLjFVGHt7G%2BrDX92UY9Gie86uNbIB58nIf1WWjnb')
    s.cookies.update(r)
    r1 = s.get("http://crmtest.bdwork.com/admin.php")
    print(r1.cookies,end=' ')
    return '登陆成功的cookies'
    r2 = s.get('http://crmtest.bdwork.com/admin.php?frames=yes&action=tools&operation=updatecache')
    print(r2.cookies)
    return '直接访问登陆后的操作页面'
add_cookies()










