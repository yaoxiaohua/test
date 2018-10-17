# coding: utf-8
from selenium import webdriver
q = 0
w = 1
phone = 13711111121
driver = webdriver.Firefox()
driver.maximize_window()
username = open('1.txt', 'a')
while q<20:
    driver.get("http://www.hfyylm.com/User/register")
    user = driver.find_element_by_id('phone_jd')
    psd = driver.find_element_by_name('regpassword')
    user.send_keys(phone)
    psd.send_keys('123456')
    ele = driver.find_element_by_id('sub_resgiter').click()
    name = driver.find_element_by_name('nickname')
    company = driver.find_element_by_name('gongsi')
    zhiwei = driver.find_element_by_name('zhiwei')
    email = driver.find_element_by_name('email')
    name.send_keys('阿斯达',w)
    company.send_keys('阿斯达',w)
    zhiwei.send_keys('阿斯达',w)
    email.send_keys('asdfg',w,'qq.com')
    ele = driver.find_element_by_id('sub_resgiter').click()
    username.writelines(['账号：',str(phone),' ','密码：123456\n'])
    w += 1
    q += 1
    phone += 1
username.close()
