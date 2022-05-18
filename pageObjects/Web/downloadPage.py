# coding=gbk
import time
from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By
from testdatas import datas as data

class DownloadPage(BasePageWeb):
    el_download_banner = (By.CSS_SELECTOR, 'div[class="download_banner"]')
    el_vx = (By.CSS_SELECTOR, 'img[src="/static/img/wx_ewm.png"]')
    el_andriodBtn = (By.CSS_SELECTOR, 'div[class="andriod_btn"]')

    el_inputClass = (By.CSS_SELECTOR, 'input[placeholder="����ؼ��������γ�"]')
    el_searchBtn = (By.CSS_SELECTOR, 'button[class ="el-button el-button--default"]')

    # ��ȡ����ҳ����
    def getDownloadUrl(self):
        self.click(loc=self.el_andriodBtn)


    # ��ȡ����ҳvxͼƬ
    def getVxPng(self,count):
        self.screenshots(str(data.shopName[count]) + 'vx')
        time.sleep(0.5)
        self.screenshotPart(scrName=str(data.shopName[count]) + 'vx', loc=self.el_vx)

    # �����γ�
    def searchClass(self,classname):
        self.input(loc=self.el_inputClass,value=classname)
        self.className = data.className
        self.click(loc=self.el_searchBtn)
        time.sleep(0.7)
