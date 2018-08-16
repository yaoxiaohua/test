# coding:utf-8
import unittest
import requests
from qihe.tests_1 import zhifubao

class TestCase(unittest.TestCase):
    #开始前打开session
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    def test_Shauxinka(self):
        '''
        支付宝刷新卡购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_1()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Qianjinding(self):
        '''
        支付宝千斤顶购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_2()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Bianseka(self):
        '''
        支付宝变色卡购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_3()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Gaimingka(self):
        '''
        支付宝改名卡购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_4()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Chakanka(self):
        '''
        支付宝查看卡购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_5()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Zhidingka(self):
        '''
        支付宝置顶卡购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_6()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Chaojihuiyuan(self):
        '''
        支付宝c超级会员购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_7()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Huiyuan(self):
        '''
        支付宝会员购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_8()
        print('刷新卡购买返回值为:%s'%q)
        #添加断言
        self.assertTrue(q["state"] == 1)

    def test_Qudaoshang(self):
        '''
        支付宝渠道商会员购买
        :return:state=1正确
        '''
        q = zhifubao.test_z_9()
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