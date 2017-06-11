# -*-coding:utf-8-*-
from time import sleep
from appium import webdriver
import unittest
import sys

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        exit_test = {}
        exit_test["platformName"] = "Android"
        exit_test["deviceName"] = "W8RDU15917001050"
        exit_test["appPackage"] = "com.sina.weibo"
        exit_test["appActivity"] = "com.sina.weibo.SplashActivity"
        exit_test["run_on_failure"] = "Capture Page Screenshot"
        exit_test["unicodeKeyboard"] = "true"
        exit_test["resetKeyboary"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",exit_test)
        sleep(25)

    # 退出
    def test_exit(self):
        wo = self.driver.find_element_by_name("我的资料")
        wo.click()
        sleep(10)

        shezhi = self.driver.find_element_by_id("titleSave")
        shezhi.click()
        sleep(5)

        zhanghaoguanli = self.driver.find_element_by_id("accountLayout")
        zhanghaoguanli.click()
        sleep(5)

        tuichu = self.driver.find_element_by_id("exitAccountContent")
        tuichu.click()

        queding = self.driver.find_element_by_name("确定")
        queding.click()
        sleep(10)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=1).run(suite)