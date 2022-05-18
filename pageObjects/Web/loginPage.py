# coding=gbk
from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By
from testdatas import datas as data

class LoginPage(BasePageWeb):

    el_phoneNum = (By.CSS_SELECTOR, "input[placeholder='请输入手机号']")
    el_passWord = (By.CSS_SELECTOR, "input[placeholder='请输入验证码']")
    el_loginBtn = (By.CSS_SELECTOR, "button[class='el-button el-button--default login']")
    el_vxBtn = (By.XPATH, '//span[contains(text(),"微信扫码登录")]')

    url = "https://www.jushispoc.com/#/phonelogin"
    loginNum = 0

    # 进入登录
    def intoLogin(self):
        self._driver.get(self.url)
        self._driver.maximize_window()

    # 登录
    def login(self):
        if data.phoneNum == '0':
            self.loginNum = self.GetPhoneNum()
            self.input(loc=self.el_phoneNum,value=self.loginNum)
        else:
            self.loginNum = data.phoneNum
            self.input(loc=self.el_phoneNum,value=self.loginNum)
        self.input(loc=self.el_passWord,value="911106")
        self.click(loc=self.el_loginBtn)
        print(self.loginNum)
        return self.loginNum

    # 使用微信登录
    def vxLogin(self):
        self.click(loc=self.el_vxBtn)

