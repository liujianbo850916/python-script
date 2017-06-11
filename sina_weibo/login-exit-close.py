#coding=utf-8
import os
import unittest
from time import sleep
import sys
from appium import webdriver


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
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', denglu_test)
        sleep(25)

    # def tearDown(self):
    #     self.driver.quit()

    # def test_login_exit(self):
    #     #点击"登录"
    #     ljb = self.driver.find_element_by_name("登录")
    #     ljb.click()
    #
    #     #输入"用户名"
    #     username = self.driver.find_element_by_id("etLoginUsername")
    #     username.send_keys("17600901055")
    #
    #     #输入"密码"
    #     pwd = self.driver.find_element_by_id("etPwd")
    #     pwd.send_keys("ljb850916")
    #
    #     #点击"登录"按钮
    #     button = self.driver.find_element_by_id("rlLogin")
    #     button.click()
    #     sleep(10)


    def test_getSize(self):
        x = self.__getattribute__()["width"]
        y = self.__getattribute__()["height"]
        return(x,y)

    def test_swipeDown(t):
        ljb = t.getSize()
        x = int(1[0] * 0.5)
        y = int(1[1] * 025)
        y1 = int(1[1] * 0.75)
        t.getSize.swipe(x, y, x, y1, t)
        sleep(5)


        # # 退出
        # wo = self.driver.find_element_by_name("我的资料")
        # wo.click()
        # sleep(10)
        #
        # shezhi = self.driver.find_element_by_id("titleSave")
        # shezhi.click()
        # sleep(5)
        #
        # zhanghaoguanli = self.driver.find_element_by_id("accountLayout")
        # zhanghaoguanli.click()
        # sleep(5)
        #
        # tuichu = self.driver.find_element_by_id("exitAccountContent")
        # tuichu.click()
        #
        # queding = self.driver.find_element_by_name("确定")
        # queding.click()
        # sleep(10)

        # #点击"我"
        # exit = self.driver.find_element_by_name("我的资料")
        # exit.click()
        #
        # #点击"设置"
        # shezhi = self.driver.find_element_by_name("设置")
        # shezhi.click()
        #
        # #点击"账号管理"
        # zhanghao = self.driver.find_element_by_id("accountLayout")
        # zhanghao.click()
        #
        # #点击"退出当前账号"
        # tuichu = self.driver.find_element_by_id("exitAccountContent")
        # tuichu.click()
        #
        # #点击"确定"
        # queding = self.driver.find_element_by_name("确定")
        # queding.click()
        # sleep(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    # assert isinstance(suite, object)
    unittest.TextTestRunner(verbosity=1).run(suite)