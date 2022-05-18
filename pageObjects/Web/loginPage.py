# coding=gbk
from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By
from testdatas import datas as data

class LoginPage(BasePageWeb):

    el_phoneNum = (By.CSS_SELECTOR, "input[placeholder='�������ֻ���']")
    el_passWord = (By.CSS_SELECTOR, "input[placeholder='��������֤��']")
    el_loginBtn = (By.CSS_SELECTOR, "button[class='el-button el-button--default login']")
    el_vxBtn = (By.XPATH, '//span[contains(text(),"΢��ɨ���¼")]')

    url = "https://www.jushispoc.com/#/phonelogin"
    loginNum = 0

    # �����¼
    def intoLogin(self):
        self._driver.get(self.url)
        self._driver.maximize_window()

    # ��¼
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

    # ʹ��΢�ŵ�¼
    def vxLogin(self):
        self.click(loc=self.el_vxBtn)

