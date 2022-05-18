# coding=gbk
from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By

class ClassDetailPage(BasePageWeb):
    el_className = (By.CSS_SELECTOR, 'div[class="sku_name"]')
    el_apply = (By.XPATH, '//span[contains(text(),"立刻报名")]')

    # 获取班级名
    def getClassText(self):
        return self.getText(loc=self.el_className)

    # 提交去订单确认页
    def apply(self):
        self.click(loc=self.el_apply)
