# #coding=utf-8
# import unittest
# from appium import webdriver
# from time import sleep
#
# class ContactsAndroidTests(unittest.TestCase):
#
#     def setUp(self):
#         getinto={}
#         getinto['platformName']='Android'
#             #平台名字=安卓
#         getinto['platformVersion']='4.4.4'
#             #平台版本=4.4.4
#         getinto['deviceName']='5a20c8c'
#             #设备名称=5a20c8c
#         getinto['appPackage']='com.sina.weibo'
#             #安装包=xxx
#         getinto['appActivity']='com.sina.weibo.SplashActivity'
#             #app活动=微博入口文件名
#         self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',getinto)
#             #这个对象的驱动方法=测试用例远程操作
#     def test_zz(self):
#         # self.signin()
#         # self.fas()
#         self.tuichu()




#coding=utf-8
import unittest
from appium import webdriver
from time import sleep


class AndroidTests(unittest.TestCase):

    def setUp(self):
        getinto={}
        # 平台名字=安卓
        getinto['platformName']='Android'
        # 平台版本=4.4.4
        getinto['platformVersion']='4.4.4'
        # 设备名称=5a20c8c
        getinto['deviceName']='455915f37d82'
        # 安装包=xxx
        getinto['appPackage']='com.sina.weibo'
        # app活动=微博入口文件名
        getinto['appActivity']='com.sina.weibo.SplashActivity'
        # 这个对象的驱动方法=测试用例远程操作
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',getinto)

    def test_zz(self):
        self.signin()
        self.fas()
        self.tuichu()

    def signin(self):
        sleep(20)
        self.driver.find_element_by_name('登录').click()
        self.driver.find_element_by_id('etLoginUsername').send_keys('176009010155')
        sleep(3)
        self.driver.find_element_by_id('etPwd').send_keys('ljb850916')
        sleep(3)
        self.driver.find_element_by_name('登录').click()
        sleep(15)
        Verification=self.driver.find_element_by_name('春风冷8').text
        self.assertEqual(u'春风冷8', Verification)

    def fas(self):
        sleep(5)
        self.driver.find_element_by_id('plus_icon').click()
        self.driver.find_element_by_id('composer_item_image').click()
        self.driver.find_element_by_name('分享新鲜事...').send_keys('aaabbbccc')
        self.driver.find_element_by_id('titleSave').click()
        el = self.driver.find_elements_by_xpath(xpath="//android.widget.TextView")
        self.assertIn(u"aaabbbccc", el[4].text)

    def lookup(self,by,locator):
        try:
            if by == 'id':
                self.driver.find_element_by_id(locator)
                return True
            elif by == 'name':
                self.driver.find_element_by_name(locator)
                return True
            elif by == 'content':
                self.driver.find_element_by_accessibility_id(locator)
                return True
                excVerification=self.driver.find_element_by_name('春风冷8').text
                self.assertEqual(u'春风冷8', Verification)

        # def test_zz(self):
        #     self.signin()
        #     self.fas()
        #     self.tuichu()


        def tuichu(self):
            my_button = self.lookup("content", "我的资料")

            while my_button is False:
                self.driver.press_keycode(4)
                my_button = self.lookup("content", "我的资料")
            self.driver.find_element_by_name('我的资料').click()
            self.driver.find_element_by_name('设置').click()
            self.driver.find_element_by_name('帐号管理').click()
            self.driver.find_element_by_name('退出当前帐号').click()
            self.driver.find_element_by_name('确定').click()

        def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


    # def lookup(self, by, locator):
    #     try:
    #         if by == 'id':
    #             self.driver.find_element_by_id(locator)
    #             return True
    #         elif by == 'name':
    #             self.driver.find_element_by_name(locator)
    #             return True
    #         elif by == 'content':
    #             self.driver.find_element_by_accessibility_id(locator)
    #             return True
    #     except:
    #         return False

    # def tuichu(self):
    #     my_button = self.lookup("content", "我的资料")
    #
    #     while my_button is False:
    #         self.driver.press_keycode(4)
    #         my_button = self.lookup("content", "我的资料")
    #     self.driver.find_element_by_name('我的资料').click()
    #     self.driver.find_element_by_name('设置').click()
    #     self.driver.find_element_by_name('帐号管理').click()
    #     self.driver.find_element_by_name('退出当前帐号').click()
    #     self.driver.find_element_by_name('确定').click()
        # 这是根据小方法写的退出脚本，意思就是找content
        # ", "
        # 我的资料
        # "这个元素，找不到就进入while循环/self.driver.press_keycode(4)这句的意思就是找不到元素就点击手机的物理键（返回键）4就是
        # 返回键/下边就是接着找content", "我的资料"找不到就接着返回

    #     def element_is_present(self, by, locator):
    #    # 这是两个形参，你懂的
    #       try:  # 尝试
    #           if by == "id":  # 如果形参是id的话就返回位真
    #               self.driver.find_element_by_id(locator)
    #               return True
    #           elif by == 'name':
    #               self.driver.find_element_by_name(locator)
    #               return True
    #           elif by == 'content':
    #               self.driver.find_element_by_accessibility_id(locator)
    #               return True
    #       except:  # 不是以上属性的就返回为假
    #           return False
    #
    #
    #   def login_tc(self):
    # # 这是两个实参和形参相对应的，如果前边输入‘id’后边‘idde参数’他就为你序找id；如果输入的是name就寻找name
    #       my_button = self.element_is_present("content", "我的资料")  # 寻找我的资料
    #
    #       while my_button is False:  # 如果当前页面不存在退出入口就进入循环
    #           self.driver.press_keycode(4)  # 找不到就点击返回键（4是手机物理键）
    #           my_button = self.element_is_present("content", "我的资料")  # 寻找content desc de txst
    #     # 找不到就一直循环
    #
    #           self.driver.find_element_by_name('我的资料').click()  # 找到后点击






