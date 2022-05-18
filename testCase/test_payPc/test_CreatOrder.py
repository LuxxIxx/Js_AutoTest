# coding=gbk
import os.path
import unittest,subprocess,time
from pageObjects.Web.homePage import HomePage
from pageObjects.Web.loginPage import LoginPage
from pageObjects.Web.classPage import ClassPage
from pageObjects.Web.classDetailPage import ClassDetailPage
from pageObjects.Web.orderAffirm import OrderAffirm
from pageObjects.Web.payPage import PayPage
from testdatas import datas as data
from BeautifulReport import BeautifulReport as bf

class test_CreatOrder0(unittest.TestCase):
    count = 0

    @classmethod
    def setUpClass(cls):
        cls.homePage = HomePage()
        cls.loginPage = LoginPage()
        cls.classPage = ClassPage()
        cls.classDetailPage = ClassDetailPage()
        cls.orderAffirm = OrderAffirm()
        cls.payPage = PayPage()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        if data.isPay:
            os.system('python test_payByPhone.py')
        time.sleep(3)

    def setUp(self):
        time.sleep(0.7)

    def tearDown(self):
        time.sleep(0.5)

    def test01_login(self):
        self.homePage.intoHome(self.count)
        self.homePage.intoLogin()
        globals()['loginNum'] = self.loginPage.login()
        time.sleep(0.5)
        assert str(self.homePage.getLoginText()) == "登录成功"


    def test02_intoClass(self):

        self.homePage.intoClassList()
        # 测试环境无法搜索，正式取消注释
        self.classPage.searchClass(data.className)

        time.sleep(0.5)
        self.classPage.intoFirstClass()
        time.sleep(0.3)
        assert str(self.classDetailPage.getClassText()) == data.className

    def test03_subOrder(self):
        self.classDetailPage.apply()
        # # if地址
        time.sleep(1)
        self.orderAffirm.sendAddr(globals()['loginNum'])
        self.orderAffirm.subOrder()


    def test04_screenshots(self):
        self.payPage.screenshots('pay')
        scrEnd = subprocess.getoutput("dir ../screenshots/pay.png /s/b")
        self.assertNotIn('找不到文件',scrEnd,'未找到截图')




# <editor-fold desc="其他商户">

class test_CreatOrder1(test_CreatOrder0):
    count = 1

class test_CreatOrder2(test_CreatOrder0):
    count = 2

class test_CreatOrder3(test_CreatOrder0):
    count = 3

class test_CreatOrder4(test_CreatOrder0):
    count = 4

class test_CreatOrder5(test_CreatOrder0):
    count = 5

class test_CreatOrder6(test_CreatOrder0):
    count = 6

class test_CreatOrder7(test_CreatOrder0):
    count = 7

class test_CreatOrder8(test_CreatOrder0):
    count = 8

class test_CreatOrder9(test_CreatOrder0):
    count = 9

class test_CreatOrder10(test_CreatOrder0):
    count = 10

# </editor-fold>

if __name__ == "__main__":
    for item in range(0, 11):
        suite = unittest.TestLoader().loadTestsFromTestCase(locals()['test_CreatOrder'+str(item)])
        run = bf(suite)
        run.report(filename=u"../report/创建订单_" + time.strftime("%Y-%m-%d_%H_%M_%S"), description=u"创建订单")


