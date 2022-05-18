# coding=gbk
from PIL import Image
from selenium import webdriver
from time import sleep
import random,time,subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

class BasePageWeb:
    def __init__(self, driver=webdriver.Chrome(service=Service(r'E:/Autotest/driver/chromedriver.exe'))):
            self._driver = driver
            self._driver.implicitly_wait(10)


    def close(self):
        sleep(20)
        self._driver.quit()

    # 定位
    def locator(self, loc):
        return self._driver.find_element(*loc)

    def locators(self, loc, count):
        return self._driver.find_elements(*loc)[count]

    # 输入
    def input(self,loc,value):
        self.locator(loc).send_keys(value)

    # 点击
    def click(self,loc):
        self.locator(loc).click()

    # 获取元素文本
    def getText(self,loc):
        return self.locator(loc).text

    def getTexts(self, loc, count):
        return self.locators(loc, count).text

    # 下拉框选择
    def comboBox(self, loc, value):
        Select(self.locator(loc)).select_by_visible_text(value)
        time.sleep(0.5)

    def comboBoxs(self, loc, count, value):
        Select(self.locators(loc, count)).select_by_visible_text(value)
        time.sleep(0.5)

    # 构造随机手机号
    def GetPhoneNum(self):
        seed = "1234567890"
        sa = []
        for i in range(9):
            sa.append(random.choice(seed))
        phoneNum = '13' + ''.join(sa)
        return phoneNum

    # 当前页面截图
    def screenshots(self,name):
        self._driver.save_screenshot(u"../screenshots/"+name+".png")
    # 指定元素截图
    def screenshotPart(self,scrName,loc):
        ele = self.locator(loc)
        top = ele.location['x']
        left = ele.location['y']
        right = top+ele.size['width']
        bottom = left+ele.size['height']
        pic = Image.open(u"../screenshots/"+scrName+".png")
        pic1 = pic.crop((top,left,right,bottom))
        pic1.save(u"../screenshots/"+scrName+".png")


    def getRequest(self):
        for request in self._driver.requests:
            if request.response and "timestamp" in request.headers:
                print(request.headers["timestamp"])







