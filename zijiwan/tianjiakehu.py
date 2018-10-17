# coding: utf-8
import requests
from bs4 import BeautifulSoup
# 定义变量，这里可以用一个
d = 1
p = 0
k = 0
Reptilian_url = []
Reptilian_title = []
# 打开session
s = requests.session()
# 伪装头部
h = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
    'accept-encoding':'gzip, deflate, br'
}
# 从第1页到最大页数的url，总共有200页，这个数值也可以从页面读取
while d in range(200):
    url = 'https://www.cnblogs.com/cate/python/%d'% d
    r = s.get(url, headers=h)
    t = r.text
    soup = BeautifulSoup(t, 'lxml')
    list = soup.select('div.post_item_body h3')
    list2 = soup.find_all(attrs={'class':"titlelnk"})
    while p < d:
        # 把标题写入空列表
        for z1 in list:
            Reptilian_title.append(z1.string)
        # 把url写入空列表
        for u1 in list2:
            Reptilian_url.append(u1['href'])
        p += 1
    d += 1
# 打印爬取的总数据量
print(len(Reptilian_title))
# 加入筛选条件，包含爬虫字段的帖子
Reptilian = open('Reptilian.txt', 'a')
while k < len(Reptilian_title):
    if '爬虫' in Reptilian_title[k]:
        print(k+1,'%s'%Reptilian_title[k],'','%s'%Reptilian_url[k])
        print('===============================')
        Reptilian.writelines(['标题：%s'%Reptilian_title[k], '\n', 'URL：%s'%Reptilian_url[k],'\n==================================\n'])
    k += 1
Reptilian.close()





