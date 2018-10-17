# # coding:utf-8
#
import requests
import time
# #定义一个类
# class shua():
#     def __init__(self,s):
#         self.s = requests.session()
#     #登陆的函数封装
#     def login(self,url):
#         self.url = 'http://crmtest.bdwork.com/appapi.php'
#         body = {
#             'mod':'phone_login',
#             'account':'吕振华',
#             'password':123456,
#             'clientId':'1b9555c2eea891c84c48805ff6d1ca56',
#             'maplat':31.091537475585938,
#             'maplon':121.52013397216797
#         }
#         a = self.s.post(self.url,data=body)
#         z=a.json()['state']
#         # if z == '1':
#         #     print('登陆成功............')
#         # else:
#         #     print('登录失败.............')
#         #     print('正在加载原因,倒计时开始，3')
#         #     time.sleep(1)
#         #     print('正在加载原因,倒计时开始，2')
#         #     time.sleep(1)
#         #     print('正在加载原因,倒计时开始，1')
#         #     time.sleep(1)
#         #     print(a.json()['msg'])
#         #     auth = a.json()
#         # time.sleep(1)
#         return a.json()['auth']
#     #刷新的函数封装
#     def shauxin(self):
#         #调用login方法返回的auth值
#         auth = shua.login(self,url='http://crmtest.bdwork.com/appapi.php')
#         body2 = {
#             'mod':'forum_forumDetailInfo',
#             'uid':314948,
#             'auth':auth,
#             'tid':28052,
#             'page':1
#         }
#         b = self.s.post(self.url,data=body2)
#         x=b.json()['state']
#         #time.sleep(1)
#         #if x == 1:
#             #print('刷新成功............')
#             #print('当前查看数为',b.json()['info']['views'])
#         #else:
#             #print('刷新失败.............')
#             #time.sleep(1)
#             #print('打印刷新状态,请稍等。。。。')
#             # time.sleep(1)
#             #print(x)
#         #time.sleep(1)
#         return '刷新完成',print('当前查看数为',b.json()['info']['views'])
# #q=info,w=views
# #类的实例化
# k = shua(s=requests.session())
# #打印调用的方法
# while 1>0:
#     print(k.shauxin())
auth = input('请输入登陆时返回的auth值')
uid = input('请输入你的uid')
tid = input('请输入帖子的tid')
print('开始刷新')
s=requests.session()
url='http://crmtest.bdwork.com/appapi.php'
body2 = {
    'mod': 'forum_forumDetailInfo',
    'uid': uid,
    'auth': auth,
    'tid': tid,
    'page': 1
}
while 1>0:
    b = s.post(url, data=body2)
    print('当前查看数为',b.json()['info']['views'])
# time.sleep(1)
# if x == 1:
# print('刷新成功............')
# print('当前查看数为',b.json()['info']['views'])
# else:
# print('刷新失败.............')
# time.sleep(1)
# print('打印刷新状态,请稍等。。。。')
# time.sleep(1)
# print(x)
# time.sleep(1)

