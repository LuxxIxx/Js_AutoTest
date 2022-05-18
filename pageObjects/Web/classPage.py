# coding=gbk
import time

from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By
from testdatas import datas as data

# �γ��б�
class ClassPage(BasePageWeb):
    el_login = (By.XPATH, '//*[@id="app"]/div[1]/div/div/div[2]/div[2]/div/div/div[2]')


    el_inputClass = (By.CSS_SELECTOR, 'input[placeholder="����ؼ��������γ�"]')
    el_searchBtn = (By.CSS_SELECTOR, 'button[class ="el-button el-button--default"]')



    el_firstClass = (By.CSS_SELECTOR, 'div[class="courseitem"]:first-child')
    el_firstClassText = (By.CSS_SELECTOR, 'div[class="courseitem"]:first-child>div>div>h1')
    el_lastClass = (By.CSS_SELECTOR, 'div[class="courseitem"]:last-child')
    el_lastClassText = (By.CSS_SELECTOR, 'div[class="courseitem"]:last-child>div>div>h1')

    el_firstClass2 = (By.CSS_SELECTOR, 'div[class="courselist clearfix"]:first-child')
    el_firstClassText2 = (By.CSS_SELECTOR, 'div[class="courselist clearfix"]:first-child>div>div>h1')
    el_lastClass2 = (By.CSS_SELECTOR, 'div[class="courselist clearfix"]:last-child')
    el_lastClassText2 = (By.CSS_SELECTOR, 'div[class="courselist clearfix"]:last-child>div>div>h1')

    # ȥ��½
    def login(self):
        self.click(loc=self.el_login)

    # �����༶
    def searchClass(self,classname):
        self.input(loc=self.el_inputClass,value=classname)
        self.className = data.className
        self.click(loc=self.el_searchBtn)
        time.sleep(0.7)

    # ��ȡ����������һ���༶��
    def firstClassName(self):
        try:
            return self.getText(loc=self.el_firstClassText)
        except:
            return self.getText(loc=self.el_firstClassText2)

    # ��ȡ����������һ���༶��
    def lastClassName(self):
        try:
            return self.getText(loc=self.el_lastClassText)
        except:
            return self.getText(loc=self.el_lastClassText2)

    # �����׸��༶
    def intoFirstClass(self):
        try:
            self.click(loc=self.el_firstClass)
        except:
            self.click(loc=self.el_firstClass2)




