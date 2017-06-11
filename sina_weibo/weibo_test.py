# coding=utf-8
# 引入模块
import client
import os
import unittest
import time
from time import sleep

from appium import webdriver

from unittest import TestCase


# 设置class
class ContactsAndroidTests(unittest.TestCase):
    # 添加方法，初始化信息（参数）
    def setUp(self):
        weibo_test = {}
        weibo_test["platformName"] = "Android"
        weibo_test["deviceName"] = "T7K6R14721000862"
        weibo_test["appPackage"] = "com.sina.weibo"
        weibo_test["appActivity"] = "com.sina.weibo.SplashActivity"
        weibo_test["run_on_failure"] = "Capture Page Screenshot"
        weibo_test["unicodeKeyboard"] = "true"
        weibo_test["resetKeyboary"] = "true"
        # 添加appium服务器地址
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",weibo_test)

        sleep(25)

    # 添加方法（登录）
    def test_login(self):
        # 登录元素id
        ljb = self.driver.find_element_by_id("titleSave")
        # 点击
        ljb.click()
        # 登录输入框元素id
        username = self.driver.find_element_by_id("etLoginUsername")
        # 输入用户名
        username.send_keys("17600901055")
        # 登录密码输入框元素id
        pwd = self.driver.find_element_by_id("etPwd")
        # 输入密码
        pwd.send_keys("ljb850916")

        # 查找登录按钮元素id
        button = self.driver.find_element_by_id("rlLogin")
        # 点击
        button.click()
        # 等待时间20
        time.sleep(20)

        # 断言-验证登录是否成功
        # self.assertEquals(self.driver.find_element("name","关注"))



    # def test_Weibo(self):
    #     button = self.driver.find_element_by_name("微博")
    #     button.click()
    #     sleep(10)
    #
    # def test_HuodongShuaxin(self):
    #     yanzheng = self.driver.swipe(self,580,365,580,1365)
    #     sleep(10)




        # 清理退出
        def tearDown(self):
            print "退出清理"

    # # 退出
    # def tuichu(self):
    #     tuichu = self.driver.page_source("关闭")









if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)