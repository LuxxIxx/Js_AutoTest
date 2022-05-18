# coding=gbk
from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By

class PayPage(BasePageWeb):
    el_className = (By.CSS_SELECTOR, 'span[class="first long-content"]')

    # 获取支付页面的班级名
    def getClassText(self):
        return self.getText(loc=self.el_className)




