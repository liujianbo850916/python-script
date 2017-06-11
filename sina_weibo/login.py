# coding=utf-8
import client
import sys
import unittest
from time import sleep
from appium import webdriver
from unittest import TestCase

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        denglu_test = {}
        denglu_test["platformName"] = "Android"
        denglu_test["deviceName"] = "455915f37d82"
        denglu_test["appPackage"] = "com.sina.weibo"
        denglu_test["appActivity"] = "com.sina.weibo.SplashActivity"
        denglu_test["run_on_failure"] = "Capture Page Screenshot"
        denglu_test["unicodeKeyboard"] = "true"
        denglu_test["resetKeyboary"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",denglu_test)
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
        sleep(25)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=1).run(suite)
