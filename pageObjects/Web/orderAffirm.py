# coding=gbk
from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By
import time
from testdatas import datas as data

# 订单确认页
class OrderAffirm(BasePageWeb):


    el_subOrderBtn = (By.CSS_SELECTOR, "div[class='placeorder_submit']")
    el_bank = (By.XPATH, '//span[contains(text(),"银联聚合")]')
    el_agreeService = (By.XPATH, '//span[contains(text(),"同意本条款,继续支付")]')

    el_isAddr = (By.CSS_SELECTOR, 'div[class="placeorder_main_title"]>span')
    el_addrTextCount = 3

    el_addrText = (By.XPATH, '//span[contains(text(),"添加收货信息")]')
    el_addrName = (By.CSS_SELECTOR, 'input[placeholder="请填写收货人姓名"]')
    el_addrProvince = (By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")
    el_addrProvinceCount = 0
    el_addrCity =(By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")
    el_addrCityCount = 1
    el_addrRegion =(By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")
    el_addrRegionCount = 2
    el_addr = (By.CSS_SELECTOR, 'input[placeholder="请填写详细地址"]')
    el_addrPhone = (By.CSS_SELECTOR, 'input[placeholder="请填写收货人电话"]')
    el_addrSaveBtn = (By.CSS_SELECTOR, "div[class='save_btu']")


    def importConsignee(self):
        pass


    def sendAddr(self, addrPhone):
        if self.getTexts(loc=self.el_isAddr, count=self.el_addrTextCount) == '添加收货信息':
            self.click(loc=self.el_addrText)
            time.sleep(0.5)
            self.input(loc=self.el_addrName, value='测试账号')
            self.comboBoxs(loc=self.el_addrProvince, count=self.el_addrProvinceCount, value='北京市')
            self.comboBoxs(loc=self.el_addrCity, count=self.el_addrCityCount, value='北京市')
            self.comboBoxs(loc=self.el_addrRegion, count=self.el_addrRegionCount, value='丰台区')
            self.input(loc=self.el_addr, value='测试地址')
            self.input(loc=self.el_addrPhone, value=addrPhone)
            time.sleep(0.5)
            self.click(loc=self.el_addrSaveBtn)
            time.sleep(0.7)
        else:
            pass


    # 选择支付方式 + 去支付 （需分离）
    def subOrder(self):
        if data.isBank == True:
            self.click(loc=self.el_bank)
            time.sleep(1)
        self.click(loc=self.el_subOrderBtn)
        time.sleep(7)
        self.click(loc=self.el_agreeService)
        time.sleep(1)
        self.click(loc=self.el_subOrderBtn)

