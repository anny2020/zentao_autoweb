# @Time: 2020/3/25  23:49
from unittest import TestCase
from selenium import webdriver
from pages.login_page import Login
from pages.zentao_addbug_page import Addbug
from pykeyboard import PyKeyboard


class TestAddBug(TestCase):
    ''' 添加缺陷  '''

    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Firefox()
        cls.addbug = Addbug(cls.driver)
        cls.login = Login(cls.driver)


    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login.html")

    # def tearDown(self):
    #     self.login.is_alert()
    #     self.driver.delete_all_cookies()
    #     self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_addbug_1(self):
        ''' 添加BUG成功'''
        self.addbug.login()
        self.addbug.add_the_bug()
        result = self.addbug.add_bug_success()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


