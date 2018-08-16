# coding:utf-8
from bs4 import BeautifulSoup
import unittest
import requests
from qihe.tests_1 import login,shuaxinka,qianjinding,bianseka,gaimingka,chakanka,chaojihuiyuan,putonghuiyuan,qudaoshanghuiyuan,baozhengjin,guanggao,zhidingka,qudaoshangquding

class TestCase(unittest.TestCase):
    #开始前打开session
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    def test_Shauxinka(self):
        '''
        刷新卡购买
        :return: 当state=1时通过
        '''
        #调用登陆方法，提取auth值
        auth = login.Login(self.s)
        q = shuaxinka.test_g_1(auth)
        print('刷新卡购买返回状态为:%s'%q)
        #添加断言
        self.assertTrue(q == '{"state":1}')

    def test_Qianjinding(self):
        '''
        千斤顶购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        w = qianjinding.test_g_2(auth)
        print('千斤顶购买返回状态为:%s'%w)
        #添加断言
        self.assertTrue(w == '{"state":1}')

    def test_Bianseka(self):
        '''
        变色卡购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        e = bianseka.test_g_3(auth)
        print('变色卡购买返回状态为:%s' %e)
        # 添加断言
        self.assertTrue(e == '{"state":1}')

    def test_Gaimingka(self):
        '''
        改名卡购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        t = gaimingka.test_g_4(auth)
        print('改名卡购买返回状态为:%s' %t)
        # 添加断言
        self.assertTrue(t == '{"state":1}')

    def test_Chakanka(self):
        '''
        查看卡购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        y = chakanka.test_g_5(auth)
        print('查看卡购买返回状态为:%s' %y)
        # 添加断言
        self.assertTrue(y == '{"state":1}')

    def test_Chaojihuiyuan(self):
        '''
        超级会员购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        u = chaojihuiyuan.test_g_6(auth)
        print('超级会员购买返回状态为:%s' %u)
        # 添加断言
        self.assertTrue(u == '{"state":1}')

    def test_Putonghuiyuan(self):
        '''
        普通会员购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        i = putonghuiyuan.test_g_7(auth)
        print('普通会员购买返回状态为:%s' %i)
        # 添加断言
        self.assertTrue(i['state'] == 1)

    def test_Qudaoshanghuiyuan(self):
        '''
        渠道商会员购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        o = qudaoshanghuiyuan.test_g_8(auth)
        print('渠道商会员购买返回状态为:%s' %o)
        # 添加断言
        self.assertTrue(o == '{"state":1}')

    def test_Baozhengjin(self):
        '''
        保证金支付
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        p = baozhengjin.test_g_9(auth)
        print('保证金支付返回状态为:%s' %p)
        # 添加断言
        self.assertTrue(p['state'] == 1)

    def test_Guanggaofei(self):
        '''
        广告费支付
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        a = guanggao.test_g_10(auth)
        print('广告费支付返回状态为:%s' %a)
        # 添加断言
        self.assertTrue(a['state'] == 1)

    def test_Zhidingka(self):
        '''
        置顶卡购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        d = zhidingka.test_g_11(auth)
        print('置顶卡购买返回状态为:%s' %d)
        # 添加断言
        self.assertTrue(d['state'] == 1)

    def test_qudaoshangZhidingka(self):
        '''
        渠道商置顶卡购买
        :return: 当state=1时通过
        '''
        auth = login.Login(self.s)
        f = qudaoshangquding.test_g_12(auth)
        print('渠道商置顶卡购买返回状态为:%s' %f)
        # 添加断言
        self.assertTrue(f['state'] == 1)

    #结束后关闭session
    @classmethod
    def tearDownClass(cls):
        cls.s.close()
# if __name__ == '__main__':
#     unittest.main()
