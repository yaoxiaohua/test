# coding:utf-8
import unittest
import requests
from qihe.tests_1 import weixin

class TestCase(unittest.TestCase):
    #开始前打开session
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    def test_Shauxinka(self):
        '''
        微信刷新卡购买
        :return:state=1正确
        '''
        q = weixin.test_w_1()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Qianjinding(self):
        '''
        微信千斤顶购买
        :return:state=1正确
        '''
        q = weixin.test_w_2()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Bianseka(self):
        '''
        微信变色卡购买
        :return:state=1正确
        '''
        q = weixin.test_w_3()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Gaimingka(self):
        '''
        微信改名卡购买
        :return:state=1正确
        '''
        q = weixin.test_w_4()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Chakanka(self):
        '''
        微信查看卡购买
        :return:state=1正确
        '''
        q = weixin.test_w_5()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Zhidingka(self):
        '''
        微信置顶卡购买
        :return:state=1正确
        '''
        q = weixin.test_w_6()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Chaojihuiyuan(self):
        '''
        微信c超级会员购买
        :return:state=1正确
        '''
        q = weixin.test_w_7()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Huiyuan(self):
        '''
        微信会员购买
        :return:state=1正确
        '''
        q = weixin.test_w_8()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Qudaoshang(self):
        '''
        微信渠道商会员购买
        :return:state=1正确
        '''
        q = weixin.test_w_9()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    #结束后关闭session
    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__ in '__main__':
    try:
        unittest.main()
    except:
        print('---------------')
