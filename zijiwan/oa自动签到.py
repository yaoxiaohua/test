# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()  # 初始化一个火狐浏览器实例：driver

driver.maximize_window()  # 最大化浏览器

#time.sleep(5)  # 暂停5秒钟

driver.get("http://oa.bdwoke.com/")  # 通过get()方法，打开一个url站点

ele = driver.find_element_by_class_name('form-control')  #找到用户名输入框

ele.send_keys('lvzhenhua')  #输入用户名

ele = driver.find_element_by_id('password')  #找到password输入框

ele.send_keys("bdwork.com")  #输入密码

ele = driver.find_element_by_id('submit')  #找到登陆按钮

ele.send_keys(Keys.ENTER)  #点击登陆按钮 ， 登陆系统成功

