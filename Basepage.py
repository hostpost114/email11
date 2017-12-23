#coding=utf-8
##############################
#Author:lixiang
#DATA:2017.10.24
#Function Description: 封装关于元素操作的一些公共方法
##############################
from selenium.webdriver.support.ui import WebDriverWait
import time,os
class Base_page(object):
    def __init__(self, driver):
        self.driver = driver
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print("%s未找到%s" % (self,loc))
    def send_keys(self, loc, value, clear_first=True, clik_first=True):
        try:
            if clik_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s未找到%s" % (self, loc))
    def click(self, loc):
        try:
            self.find_element(*loc).click()
            time.sleep(2)
        except AttributeError:
            print("%s未找到%s" % (self, loc))

    def get_screenshot(self):
        dir_path = 'E:\/'
        pic_name = time.strftime('%Y%m%d%H%M%S') + '.png'
        pic_url = dir_path + pic_name
        try:
            self.driver.save_screenshot(pic_url)
            print('screenshot_name:%s' % pic_name)
        except:
            raise

