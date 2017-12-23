from POM.Basepage import *
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
"""
封装登录页面的元素

"""
class loging(Base_page):
    #密码框的按钮
    pasw_icon=(By.ID,'hb')
    #登录按钮
    denglu_icon=(By.ID,'blk')
    #shuru密码
    def input_passw(self,passw):
        self.send_keys(self.pasw_icon,passw)
        sleep(2)
    #点击确认登录按钮
    def loging_enter(self):
        self.click(self.denglu_icon)