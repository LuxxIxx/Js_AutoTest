# coding=gbk
import datetime,xlrd,unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

class test_ToCompanyOrder(unittest.TestCase):

    # <editor-fold desc="夹具">
    @classmethod
    def setUpClass(cls):
        book = xlrd.open_workbook(r'E:/AutoTest/testdatasdata/creatorder.xlsx')
        date = book.sheet_by_index(0)
        dateList = date.row_values(1)
        cls.count = date.nrows
        # 赋值
        cls.url = str(dateList[0]).strip('\r\n\t')
        cls.shop = str(dateList[1]).strip('\r\n\t')
        cls.phone = str(dateList[2]).strip('\r\n\t')
        cls.name = str(dateList[3]).strip('\r\n\t')
        cls.addr = str(dateList[4]).strip('\r\n\t')
        cls.product = str(dateList[5]).strip('\r\n\t')
        cls.orderNum = 0
        if len(cls.url) == 0:
            cls.url = 'https://t1-jspc.gzjushiwang.com/#/clazzCourseDetail/1507173532602933249/1507173455721340929/1'
        if len(cls.phone) == 0:
            cls.phone = 13000000001
        else:
            cls.phone = int(dateList[2])
        if len(cls.name) == 0:
            cls.name = '测试人员'
        if len(cls.addr) == 0:
            cls.addr = '测试地址'

        if str(dateList[6]).strip('\r\n\t') == '是':
            cls.isPay = True
        else:
            cls.isPay = False

        cls.driver = webdriver.Chrome(service=Service(r'd:\driver\chromedriver.exe'))
        cls.driver.implicitly_wait(20)

        cls.driver.get('https://t1-jsui.gzjushiwang.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver = webdriver.Chrome(service=Service(r'd:\driver\chromedriver.exe'))
        cls.driver.quit()

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        pass

    # </editor-fold>

    # <editor-fold desc="用例">
    def test01_login(self):
        self.driver.find_elements(By.CLASS_NAME, 'ivu-input-default')[0].send_keys('17812322339')
        self.driver.find_elements(By.CLASS_NAME, 'ivu-input-default')[1].send_keys('123456')
        self.driver.find_element(By.CLASS_NAME, 'ivu-btn-long').click()
        self.driver.find_element(By.CSS_SELECTOR, 'div[title="' + self.shop + '"][class="chooseInner_name"]').click()

    def test02_editOrder(self):
        self.driver.find_element(By.XPATH,'//div[@class="ivu-menu-submenu-title"]/span[contains(text(),"订单管理")]').click()
        self.driver.find_element(By.XPATH,"//li[@class='ivu-menu-item']/span[contains(text(),'添加对公支付订单')]").click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[2]/div/div/input').send_keys(self.url)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[7]/div/div[1]/input').send_keys(self.phone)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[9]/div/div[1]/input').send_keys(self.name)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[10]/div/div/input').send_keys(self.phone)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[11]/div/div').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[11]/div/div/div[2]/ul[2]/li[1]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[12]/div/div').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[12]/div/div/div[2]/ul[2]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[13]/div/div/div[1]').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[13]/div/div/div[2]/ul[2]/li[4]').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[14]/div/div/input').send_keys(self.addr)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[16]/div/button').click()

    def test03_payWay(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/span').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/ul[2]/li[2]').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/form/div[3]/div/div/div/div[1]/input').send_keys(self.name)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='file'][accept='.jpg,.png,.jpeg']").send_keys(r'E:\\自动化调试\image\test.jpg')
        time.sleep(3)

    def test04_subOrder(self):
        self.driver.find_elements(By.CSS_SELECTOR, "div[style='margin-left: 100px;']>button[type='button']")[1].click()
        # 检查

    def test05_goOrderAudit(self):
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//div[@class="ivu-menu-submenu-title"]/span[contains(text(),"订单管理")]').click()
        self.driver.find_element(By.XPATH, "//li[@class='ivu-menu-item']/span[contains(text(),'对公转账订单')]").click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[9]/div/div/input').send_keys(self.phone)
        self.driver.find_element((By.XPATH),'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[17]/div/button[1]').click()
        move = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div')
        ActionChains(self.driver).move_to_element(move).perform()
        time.sleep(0.5)
        self.driver.find_elements(By.CSS_SELECTOR, "div[class='ivu-select-dropdown ivu-dropdown-transfer']>ul>li")[6].click()

    def test06_subAudit(self):
        self.driver.find_element(By.XPATH,'//label[contains(text(),"通过")]').click()
        dateTime = datetime.date.today()
        self.driver.find_elements(By.CSS_SELECTOR, "input[class='ivu-input ivu-input-default ivu-input-with-suffix']")[2].send_keys(str(dateTime) + ' 00:00:00')
        time.sleep(2)
        enter = self.driver.find_elements(By.CSS_SELECTOR,'div[class="ivu-modal-content ivu-modal-content-drag"]>div[class="ivu-modal-footer"]>button[class="ivu-btn ivu-btn-primary"]>span')
        if len(enter) == 10:
            enter[8].click()
        else:
            enter[6].click()

        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[1]/div/div/input').clear()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[1]/div/div/input').send_keys(self.orderNum)
        self.driver.find_element((By.XPATH),'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[17]/div/button[1]').click()
        time.sleep(2)
        ischeck = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[36]/div/div/div/span').text

        # 检查ischeck
        assert ischeck




    # </editor-fold>


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(test_ToCompanyOrder("test01_login"))
    # unittest.main(defaultTest="suite")
    unittest.main()

