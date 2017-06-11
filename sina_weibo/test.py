# coding=utf-8
import unittest
from unittest import TestCase


class AndroidTest(unittest.TestCase):
    def setUp(self):
        parameter = {}
        parameter['platformName'] = 'Android'
        parameter['platformVersion'] = '4.4.4'
        parameter['deviceName'] = ''


if __name__=="__main__":
    suite= unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(test=2).run(suite)