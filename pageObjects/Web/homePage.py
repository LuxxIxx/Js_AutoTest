# coding=gbk
import time
from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By
from testdatas import datas as data

class HomePage(BasePageWeb):

    el_login = (By.XPATH, '//*[@id="app"]/div[1]/div/div/div[2]/div[2]/div/div/div[2]')
    el_class = (By.CSS_SELECTOR, 'div[class="header_main clerfix"]>div>div>div[class="nav_item"]')
    el_icon = (By.CSS_SELECTOR, 'img[src="/static/img/logo.png"]')
    el_Download = (By.XPATH, '//div[contains(text(),"APP下载")]')

    el_copyright = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div[1]/p')



    #登陆成功提示框
    el_loginText = (By.CSS_SELECTOR, "div[role='alert']>p")


    # 进入主页面
    def intoHome(self,count):
        self._driver.get(data.urlList[count])
        self._driver.maximize_window()

    def intoHome2(self,count):
        self._driver.get(data.urlList2[count])
        self._driver.maximize_window()

    # 登录入口
    def intoLogin(self):
        self.click(loc=self.el_login)
    # 班级列表入口
    def intoClassList(self):
        self.click(loc=self.el_class)
    # 下载页入口
    def intoDownload(self):
        self.click(loc=self.el_Download)

    # 验证登录成功弹窗文字
    def getLoginText(self):
        return self.getText(loc=self.el_loginText)

    # 截取主页icon图片
    def getIconPng(self,count):
        self.screenshots(str(data.shopName[count])+'icon')
        time.sleep(0.5)
        self.screenshotPart(scrName=str(data.shopName[count])+'icon',loc=self.el_icon)


    # 获取备案版权信息
    def getfile(self):
        return self.getText(self.el_copyright)





