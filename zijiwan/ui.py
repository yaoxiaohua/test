# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 初始化一个火狐浏览器实例：driver
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 通过get()方法，打开一个url站点
driver.get("http://www.bdwork.com/")

# 通过xpath定位到登陆按钮并点击
ele = driver.find_element_by_xpath('/html/body/div[5]/div/span/a[1]')
# 执行太快，无法滚动到视图中，添加等待时间
time.sleep(2)
ele.click()
# 定位并输入username，psw，添加等待时间
time.sleep(2)
ele = driver.find_element_by_xpath("//*[contains(@id,'username')]")
ele.send_keys('17621211515')
ele = driver.find_element_by_xpath("//*[contains(@id,'password')]")
ele.send_keys('147258369')
# 点击登陆按钮
ele = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[1]/div/div[1]/div/form/div/button")
ele.click()
# 登陆成功打印记录
print('-----------------\n','登陆成功\n','------------------')
print('-----------------\n','等待跳转\n','------------------')

# 等待跳转，最长10s，其中每0.5秒扫描一次是否存在指定元素
wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[(@href="/home.php?mod=space&uid=1079759")]')))
# 点击等待查找的置顶元素
wait.click()

# 获取所有窗口句柄并切换至最新打开的窗口
print('-----------------\n','切换新窗口\n','------------------')
time.sleep(2)
windows = driver.window_handles
driver.switch_to.window(windows[-1])
# 编辑我的个人资料
while 1>0:
    ele = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[2]/a[1]')
    ele.click()
# 职业认证，弹框不知道该怎么定位，先放一放(可以用按键试试)

print('-----------------\n','切换新窗口\n','------------------')
time.sleep(2)
windows = driver.window_handles
driver.switch_to.window(windows[-1])

# 点击个人中心~~~~~弹出选择图片框
ele = driver.find_element_by_xpath('/html/body/div[5]/div/ul[1]/li[1]/a')
ele.click()
ele = driver.find_element_by_xpath('/html/body/div[6]/div[1]/ul/li[9]/a')
ele.click()
ele = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/table/tbody/tr[6]/td[3]/a')
ele.click()
# ele = driver.find_element_by_xpath('//*[@id="uploadButton_1"]')
# ele.click()

# 定位弹出框
iframe = driver.find_elements_by_tag_name('imgFile')
# 切换到iframe上
driver.switch_to_frame(iframe)
# 上传图片
driver.find_element_by_name('imgFile').send_keys(r"C:\Users\bdwork15\Desktop\153414667.jpg")


