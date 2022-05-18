# coding=gbk
import unittest,subprocess,time,os
from BeautifulReport import BeautifulReport
from pageObjects.Web.homePage import HomePage
from pageObjects.Web.downloadPage import DownloadPage
from pageObjects.Web.classPage import ClassPage
from pageObjects.Web.loginPage import LoginPage
from BeautifulReport import BeautifulReport as bf
from testdatas import datas as data

class WebCopy0(unittest.TestCase):
    count = 0
    @classmethod
    def setUpClass(cls):
        cls.homePage = HomePage()
        cls.downloadPage = DownloadPage()
        cls.classPage = ClassPage()
        cls.loginPage = LoginPage()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        time.sleep(0.7)

    def tearDown(self):
        time.sleep(0.5)


    def test_01getIconScreenshots(self):
        self.homePage.intoHome(self.count)
        self.homePage.getIconPng(self.count)
        print('请返回截图目录确认icon')

    def test_02file(self):
        file = self.homePage.getfile()
        print(file.strip())
        assert file.strip() == data.file[self.count].strip()

    def test_03download(self):
        self.homePage.intoDownload()
        time.sleep(1.5)
        self.downloadPage.getDownloadBanner(self.count)
        self.downloadPage.getVxPng(self.count)
        print('请返回截图目录确认二维码')
        print('请返回截图目录确认下载页文案')

    def test_04searchPrecise(self):
        self.downloadPage.searchClass(data.className)
        print(self.classPage.firstClassName())
        print(self.classPage.lastClassName())
        assert self.classPage.firstClassName() == self.classPage.lastClassName() == data.className

    def test_05searchDim(self):
        self.classPage.searchClass(data.classNamePart)
        time.sleep(0.7)
        print(self.classPage.firstClassName())
        print(self.classPage.lastClassName())
        assert data.classNamePart in self.classPage.firstClassName() and data.classNamePart in self.classPage.lastClassName()

    def test_06creatClass(self):
        print('需要改动线上数据')

    def test_07vxLogin(self):
        print('微信不支持相册识别登录')
        # self.classPage.login()
        # self.loginPage.vxLogin()
        # self.loginPage.screenshots('vx')
        # os.system('python test_loginByPhone.py')
        # try:
        #     assert data.classNamePart in self.classPage.firstClassName() and data.classNamePart in self.classPage.lastClassName()
        # except:
        #     assert 1 > 2

class WebCopy1(WebCopy0):
    count = 1
class WebCopy2(WebCopy0):
    count = 2
class WebCopy3(WebCopy0):
    count = 3
class WebCopy4(WebCopy0):
    count = 4
class WebCopy5(WebCopy0):
    count = 5
class WebCopy6(WebCopy0):
    count = 6
class WebCopy7(WebCopy0):
    count = 7
class WebCopy8(WebCopy0):
    count = 8
class WebCopy9(WebCopy0):
    count = 9
class WebCopy10(WebCopy0):
    count = 10






if __name__ == "__main__":
    for item in range(0,11):
        suite = unittest.TestLoader().loadTestsFromTestCase(locals()['WebCopy'+str(item)])
        run = bf(suite)
        run.report(filename=u"../report/webCopy/"+data.shopName[item]+"复制验证_" + time.strftime("%Y-%m-%d_%H_%M_%S"), description=u"平台复制验证")



