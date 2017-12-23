import unittest
from POM.page import Wechat
from appium import webdriver
from HTMLTestRunner import HTMLTestRunner
from POM.logging_page import *
testcase_dir = 'E:\pycharm\Demo\First_Po\Testcase.py'
class Touch(unittest.TestCase):
    @classmethod
    def setUp(self):
        desired_caps = {
        'platformName' :'Android',
        'platformVersion': '4.4',
        'deviceName' : 'DU2SSE15C3115777',
        'appPackage' :'com.tencent.mm' ,# 'com.android.contacts'
        'appActivity': '.ui.LauncherUI',  # '.activities.DialtactsActivity'
        'unicodekeybord' : 'True',
        "resetKeyboard":"True"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(30)
        self.driver.implicitly_wait(30)
    @classmethod
    def tearDown(self):
        self.driver.quit()
    def test000(self):
        x=loging(self.driver)
        #为登录页面断言
        self.assertEqual(self.driver.find_element_by_name('2971966792').text, '2971966792')
        #输入密码
        x.input_passw('lixiang123456')
        x.loging_enter()
        sleep(4)
        self.assertEqual(self.driver.find_element_by_name('Duang').text, 'Duang')
    def test001(self):
        print('正在测试test001')
        li=Wechat(self.driver)
        li.contacts('qichuangla')
        self.assertEqual(self.driver.find_element_by_name('Duang').text,'Duang')
    def test002(self):
        print('正在测试test001')
        li=Wechat(self.driver)
        li.discover()
        li.me()

