# coding:utf-8
import requests
from bs4 import BeautifulSoup
import chardet
import pymysql.cursors
import time
from decimal import *

class Reptilian(object):
    def data(self):
        # 定义需要的数据
        saishi = []
        kedui = []
        pankou = []
        shuju = []
        # insetinto sql要用到的数据
        BF_HALF = []
        MATCH_ID = []
        BF = []
        BF_ODDS = []
        SPF = []
        SPF_ODDS = []
        RQ = []
        RQ_ODDS = []
        JQ = []
        JQ_ODDS = []
        BQC = []
        BQC_ODDS = []

        #定义一个内置浏览器session
        s = requests.session()

        # # q是存储爬取信息的文本文件，使用追加模式，就是说后面写入的信息会放在已有的信息后面，这样就不会把之前的信息覆盖掉
        # q = open('info.txt', 'a')
        url = 'http://www.310win.com/jingcaizuqiu/rangqiushengpingfu/kaijiang_jc_all.html'

        # header把爬虫伪装的像是正常的访问
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 ',
            'Connection': 'keep-alive'
            }

        # 用requests库的get方法与服务器进行链接,返回一个requests.models.Response的类
        w = s.get(url, headers=header)

        # 用chardet库的detect方法获取网页编码格式,具体的编码格式在encoding这个键对应的值中
        w.encoding = chardet.detect(w.content)['encoding']

        # 设置好编码格式后，用text方法把Response这个类转化为字符串供beautifulSoup处理
        e = w.text

        # 替换掉其中的符号'-',和换行符```这里不能替换‘-’，不然比分出来缺少，改为下面替换
        z=(e.replace('<br>','')).replace('<br/>','')

        # 使用BeautifulSoup函数把z转化为一个BeautifulSoup对象，解析器的类型是lxml
        soup = BeautifulSoup(z, 'lxml')

        # 获取class属性为ni，ni2中的td
        list = soup.select('tr.ni td')
        list2 = soup.select('tr.ni2 td')

        # 用string方法获取td标签中的数据，写进list
        a = 0
        while a < len(list2):
            for z1 in list[a]:
                MATCH_ID.append('2018'+z1.string[5:10].replace('-','')+'%s'%z1.string[2:5])
                for x1 in list[a+1]:
                    saishi.append(x1.string)
                    for c1 in list[a+3]:
                        BF.append(c1.string)
                        for v1 in list[a+4]:
                            kedui.append(v1.string)
                            for b1 in list[a+5]:
                                BF_HALF.append(b1.string)
                                for n1 in list[a-2]:
                                    pankou.append(n1.string)
                                    for m1 in list[a-1]:
                                        shuju.append(m1.string)
            for z2 in list2[a]:
                MATCH_ID.append('2018'+z2.string[5:10].replace('-','')+'%s'%z2.string[2:5])
                for x2 in list2[a+1]:
                    saishi.append(x2.string)
                    for c2 in list2[a+3]:
                        BF.append(c2.string)
                        for v2 in list2[a+4]:
                            kedui.append(v2.string)
                            for b2 in list2[a+5]:
                                BF_HALF.append(b2.string)
                                for n2 in list2[a-2]:
                                    pankou.append(n2.string)
                                    for m2 in list2[a-1]:
                                        shuju.append(m2.string)
            a = a+13

        # 用string方法获取a标签中的数据，写进list
        list3 = soup.select('tr.ni a')
        list4 = soup.select('tr.ni2 a')
        b = 2
        while b < len(list4):
            for z3 in list3[b]:
                BF_ODDS.append(z3.string)
                for x3 in list3[b-1]:
                    SPF_ODDS.append(x3.string)
                    for c3 in list3[b - 2]:
                        RQ_ODDS.append(c3.string)
                        for v3 in list3[b+1]:
                            JQ_ODDS.append(v3.string)
                            for b3 in list3[b + 2]:
                                BQC_ODDS.append(b3.string)
            for z4 in list4[b]:
                BF_ODDS.append(z4.string)
                for x4 in list4[b-1]:
                    SPF_ODDS.append(x4.string)
                    for c4 in list4[b - 2]:
                        RQ_ODDS.append(c4.string)
                        for v4 in list4[b+1]:
                            JQ_ODDS.append(v4.string)
                            for b4 in list4[b + 2]:
                                BQC_ODDS.append(b4.string)
            b = b+8

        # 用string方法获取span标签中的数据，写进list
        c = 1
        list5 = soup.select('tr.ni span')
        list6 = soup.select('tr.ni2 span')
        while c < len(list6):
            for z5 in list5[c]:
                SPF.append(z5.string)
                for x5 in list5[c-1]:
                    RQ.append(x5.string)
                    for c5 in list5[c+2]:
                        JQ.append(c5.string)
                        for v5 in list5[c + 3]:
                            BQC.append(v5.string)
            for z6 in list6[c]:
                SPF.append(z6.string)
                for x6 in list6[c-1]:
                    RQ.append(x6.string)
                    for c6 in list6[c+2]:
                        JQ.append(c6.string)
                        for v6 in list6[c + 3]:
                            BQC.append(v6.string)
            c = c+5
        return MATCH_ID,BF_HALF,BF,BF_ODDS,SPF,SPF_ODDS,RQ,RQ_ODDS,JQ,JQ_ODDS,BQC,BQC_ODDS

    # 爬取的数据
    # try:
    #     d = 0
    #     for d in range(len(MATCH_ID)):
    #         print('%s' % MATCH_ID[d],BF_HALF[d],BF[d],BF_ODDS[d],SPF[d],SPF_ODDS[d],RQ[d],RQ_ODDS[d],JQ[d],JQ_ODDS[d],BQC[d],BQC_ODDS[d])
    #         d = d+1
    # except:
    #     print('-----------------------')

    def insert(self):

        # 定义当前时间
        now = time.strftime('%Y%m%d', time.localtime())

        # 调用data的返回值，分别定义为sql所用字段
        MATCH_ID = Reptilian.data()[0],
        BF_HALF = Reptilian.data()[1],
        BF = Reptilian.data()[2],
        BF_ODDS = Reptilian.data()[3],
        SPF = Reptilian.data()[4],
        SPF_ODDS = Reptilian.data()[5],
        RQ = Reptilian.data()[6],
        RQ_ODDS = Reptilian.data()[7],
        JQ = Reptilian.data()[8],
        JQ_ODDS = Reptilian.data()[9],
        BQC = Reptilian.data()[10],
        BQC_ODDS = Reptilian.data()[11]

        # 连接数据库
        connect = pymysql.Connect(
                host = '120.26.90.177',
                port = 3306,
                user = 'test_admin',
                passwd = 'bdwork.com!@#',
                db = 'bdwork_test',
                charset = 'utf8'
            )

        # 也可以先转换数据格式，再插入变量
        # label = list((1, 2, 3, 4, 5, 6, 7, 8, 9, "10"))
        # label_A = [str(i) for i in label]
        # print(label_A)

        # 获取游标
        cursor = connect.cursor()

        # VALUES从list中第一个值开始插入，循环至最后一个值
        Value = 0
        while Value <= len(MATCH_ID[0]):
            if BF_ODDS[0][Value] != None and JQ_ODDS[0][Value] != None and RQ_ODDS[0][Value] != None and SPF_ODDS[0][Value] != None and BQC_ODDS[Value] != None:
                sql = "INSERT INTO bdwork_test.T_LOT_FOOT_MATCH_RESULT(MATCH_ID,BF_HALF,BF,SPF,RQ,JQ,BQC,SUB_TIME,UPDATE_TIME,BF_ODDS,SPF_ODDS,RQ_ODDS,JQ_ODDS,BQC_ODDS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"  %(MATCH_ID[0][Value],BF_HALF[0][Value],BF[0][Value],SPF[0][Value],RQ[0][Value],JQ[0][Value],BQC[0][Value],now,now,float(BF_ODDS[0][Value]),float(SPF_ODDS[0][Value]),float(RQ_ODDS[0][Value]),float(JQ_ODDS[0][Value]),float(BQC_ODDS[Value]))
                cursor.execute(sql)
                connect.commit()
                Value += 1
                if Value == len(MATCH_ID[0]):
                    break
            else:
                if SPF_ODDS[0][Value] == None:
                    sql = "INSERT INTO bdwork_test.T_LOT_FOOT_MATCH_RESULT(MATCH_ID,BF_HALF,BF,SPF,RQ,JQ,BQC,SUB_TIME,UPDATE_TIME,BF_ODDS,RQ_ODDS,JQ_ODDS,BQC_ODDS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"  %(MATCH_ID[0][Value],BF_HALF[0][Value],BF[0][Value],SPF[0][Value],RQ[0][Value],JQ[0][Value],BQC[0][Value],now,now,float(BF_ODDS[0][Value]),float(RQ_ODDS[0][Value]),float(JQ_ODDS[0][Value]),float(BQC_ODDS[Value]))
                    cursor.execute(sql)
                    connect.commit()
                    Value += 1
                    if Value == len(MATCH_ID[0]):
                        break
                elif BF_ODDS[0][Value] == None:
                    sql = "INSERT INTO bdwork_test.T_LOT_FOOT_MATCH_RESULT(MATCH_ID,BF_HALF,BF,SPF,RQ,JQ,BQC,SUB_TIME,UPDATE_TIME,SPF_ODDS,RQ_ODDS,JQ_ODDS,BQC_ODDS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    MATCH_ID[0][Value], BF_HALF[0][Value], BF[0][Value], SPF[0][Value], RQ[0][Value],
                    JQ[0][Value], BQC[0][Value], now, now,float(SPF_ODDS[0][Value]), float(RQ_ODDS[0][Value]),
                    float(JQ_ODDS[0][Value]), float(BQC_ODDS[Value]))
                    cursor.execute(sql)
                    connect.commit()
                    Value += 1
                    if Value == len(MATCH_ID[0]):
                        break
                elif JQ_ODDS[0][Value] == None:
                    sql = "INSERT INTO bdwork_test.T_LOT_FOOT_MATCH_RESULT(MATCH_ID,BF_HALF,BF,SPF,RQ,JQ,BQC,SUB_TIME,UPDATE_TIME,BF_ODDS,SPF_ODDS,RQ_ODDS,BQC_ODDS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    MATCH_ID[0][Value], BF_HALF[0][Value], BF[0][Value], SPF[0][Value], RQ[0][Value], JQ[0][Value],
                    BQC[0][Value], now, now, float(BF_ODDS[0][Value]),float(SPF_ODDS[0][Value]), float(RQ_ODDS[0][Value]),
                    float(BQC_ODDS[Value]))
                    cursor.execute(sql)
                    connect.commit()
                    Value += 1
                    if Value == len(MATCH_ID[0]):
                        break
                elif RQ_ODDS[0][Value] == None:
                    sql = "INSERT INTO bdwork_test.T_LOT_FOOT_MATCH_RESULT(MATCH_ID,BF_HALF,BF,SPF,RQ,JQ,BQC,SUB_TIME,UPDATE_TIME,BF_ODDS,SPF_ODDS,JQ_ODDS,BQC_ODDS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    MATCH_ID[0][Value], BF_HALF[0][Value], BF[0][Value], SPF[0][Value], RQ[0][Value], JQ[0][Value],
                    BQC[0][Value], now, now, float(BF_ODDS[0][Value]),float(SPF_ODDS[0][Value]),
                    float(JQ_ODDS[0][Value]), float(BQC_ODDS[Value]))
                    cursor.execute(sql)
                    connect.commit()
                    Value += 1
                    if Value == len(MATCH_ID[0]):
                        break
                elif BQC_ODDS[Value] == None:
                    sql = "INSERT INTO bdwork_test.T_LOT_FOOT_MATCH_RESULT(MATCH_ID,BF_HALF,BF,SPF,RQ,JQ,BQC,SUB_TIME,UPDATE_TIME,BF_ODDS,SPF_ODDS,RQ_ODDS,JQ_ODDS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    MATCH_ID[0][Value], BF_HALF[0][Value], BF[0][Value], SPF[0][Value], RQ[0][Value], JQ[0][Value],
                    BQC[0][Value], now, now, float(BF_ODDS[0][Value]), float(SPF_ODDS[0][Value]),float(RQ_ODDS[0][Value]),float(JQ_ODDS[0][Value]))
                    cursor.execute(sql)
                    connect.commit()
                    Value += 1
                    if Value == len(MATCH_ID[0]):
                        break
            print('插入第%s条数据' % Value)
        # 关闭连接
        cursor.close()
        connect.close()
        return  print('执行完成')

if __name__ == '__main__':
        Reptilian = Reptilian()
        Reptilian.insert()
