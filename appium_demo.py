#!/usr/bin/python
# coding: utf-8
import os
import time
import unittest
from appium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Lenovo P1c72'

desired_caps['app'] = PATH('C:\Users\wenkai.ding\Desktop\Fanli.apk')
#desired_caps['appPackage'] = 'com.xiangchao.starspace'　　
#desired_caps['appActivity'] = 'com.xiangchao.starspace.activity.SplashActivity'

#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
driver.swipe(0, 100, 700, 100, duration=100)
print 1
time.sleep(10)
driver.swipe(0, 100, 700, 100, duration=100)
time.sleep(10)
driver.swipe(600, 100, 0, 10, duration=100)
print 3
time.sleep(5)
x = driver.get_window_size()['width']

y = driver.get_window_size()['height']
x = int(x*0.1)
y = int(y*0.1)

driver.swipe(x, y, x, y,1)
print 4
time.sleep(3)

driver.find_element_by_id("com.fanli.android.apps:id/tv_search_hint").click()
driver.find_element_by_id("com.fanli.android.apps:id/home_search_pre_edit_head_search_edit_btn").send_keys("123456")

