# @Time: 2020/3/22  12:13
import time
from unittest import TestCase
from selenium import webdriver
from pages.login_page import Login
import ddt
testdata = [{'username':'admin','passwd':'123456','expect':'admin'},
            {'username':'admin1','passwd':'1234567','expect':''}]
@ddt.ddt
class TestZentao(TestCase):
    '''登录'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.zentaologin = Login(cls.driver)

    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login.html")

    def tearDown(self):
        Login.is_alert(self)
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


#登录成功的用例1
    def login_1(self,username,passwd,expect):
        '''登录成功'''
        self.zentaologin.input_username(username)
        self.zentaologin.input_passwd(passwd)
        self.zentaologin.keep_loginon()
        self.zentaologin.click_login()
        time.sleep(3)
        user_name = Login.get_login_username(self)
        self.assertTrue(user_name == expect)

    @ddt.data(*testdata)
    def test_case_1(self,data):
        print("--------------开始测试----------------------")
        data1 = testdata[0]
        print("测试数据是%s" % data1)
        self.login_1(data["username"],data["passwd"],data["expect"])
        print("--------------结束测试pass------------------------")

# 登录失败的用例2  错误的用户和密码
    def login_2(self,username,passwd,expect):
        '''登录失败'''
        self.zentaologin.input_username(username)
        self.zentaologin.input_passwd(passwd)
        self.zentaologin.keep_loginon(False)
        self.zentaologin.click_login()
        time.sleep(3)
        user_name = Login.get_login_username(self)
        # print(user_name)
        self.assertTrue(user_name == expect)

    # def test_case_2(self):
    #     print("--------------开始测试----------------------")
    #     data2 = testdata[1]
    #     print("测试数据是%s" % data2)
    #     self.login_1(data2["username"],data2["passwd"],data2["expect"])
    #     print("--------------结束测试pass------------------------")

    def login_3(self):
        result = self.zentaologin.forget_passwd()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

