# coding=gbk
from base.basePageWeb import BasePageWeb
from selenium.webdriver.common.by import By

class PayPage(BasePageWeb):
    el_className = (By.CSS_SELECTOR, 'span[class="first long-content"]')

    # ��ȡ֧��ҳ��İ༶��
    def getClassText(self):
        return self.getText(loc=self.el_className)




