# coding=utf-8

import sys
from time import sleep
import unittest
from appium import webdriver

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        exit_test = {}
        exit_test["platformName"] = "Android"
        exit_test["deviceName"] = "T7K6R14721000862"
        exit_test["appPackage"] = "com.sina.weibo"
        exit_test["appActivity"] = "com.sina.weibo.SplashActivity"
        exit_test["run_on_failure"] = "Capture Page Screenshot"
        exit_test["unicodeKeyboard"] = "true"
        exit_test["resetKeyboary"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",exit_test)
        sleep(20)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=1).run(suite)

