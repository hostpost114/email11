from selenium.webdriver.common.by import By
from time import sleep
from POM.Basepage import Base_page
from appium import webdriver
#8888888888888888888888888#
#微信操作界面所有元素》》操作方法》》封装
#888888888888888888888888#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitly_wait(30)
class Wechat(Base_page):
    #添加按钮
    add_loc=(By.ID,'fu')
    #微信按钮
    wechat_loc=(By.NAME,'微信')
    #通讯录按钮
    contact_loc=(By.NAME,'通讯录')
    #发现按钮
    discover_loc=(By.NAME,'发现')
    #我  按钮
    me_loc=(By.NAME,'我')
    #shezhi
    setting=(By.NAME,'设置')
    duang=(By.NAME,'Duang')
    #dianji faxiaoxi
    sentext=(By.ID,'com.tencent.mm:id/ahq')
    inputmess=(By.ID,'com.tencent.mm:id/a71')
    #点击通讯录按钮
    def contacts(self,values):
        self.click(self.contact_loc)
        sleep(0.5)
        self.get_screenshot()
        sleep(3)
        self.click(self.duang)
        self.click(self.sentext)
        self.get_screenshot()
        sleep(2)
        self.send_keys(self.inputmess,values)
        #点击发现按钮
    def discover(self):
        self.click(self.discover_loc)
        sleep(3)
        self.get_screenshot()

        #点击 “我”按钮
    def me(self):
        self.click(self.me_loc)
        sleep(3)
        self.get_screenshot()

    # def bubble(self):
#     dash_page=Wechat(Base_page)
#     dash_page.contacts()
#     sleep(2)
#     dash_page.discover()
#     sleep(2)
#     dash_page.me()
