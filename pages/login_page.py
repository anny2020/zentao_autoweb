# @Time: 2020/3/23  8:41
# from selenium import webdriver
from common.base import Base
from selenium.webdriver.support import expected_conditions as EC
import time
class Login():

    def __init__(self,driver):
        self.base = Base(driver)
        self.driver = driver
        self.loc_username = ('id','account')
        self.loc_paswd = ("name","password")
        self.loc_keeplogin = ("id","keepLoginon")
        self.loc_login = ("id","submit")
        self.loc_text = ("css selector","#userMenu>a")
        self.forget_paswd = ("link text","忘记密码")
        self.refresh = ("xpath","html/body/div[1]/div/div[2]/p/a")



    def input_username(self,username):
        self.username = username
        # self.base.find_Element(self.loc_username).send_keys(self.username)
        result = self.base.is_element_exist3(self.loc_username)
        # result = self.base.isElementExist(self.loc_username)
        if result:
            self.base.send_Keys(self.loc_username,self.username)
        else:
            print('元素%s未找到'% self.loc_username)

    def input_passwd(self,passwd):
        self.passwd = passwd
        # self.base.find_Element(self.loc_paswd).send_keys(self.passwd)
        self.base.send_Keys(self.loc_paswd,self.passwd)


    def keep_login(self):
        # self.base.find_Element(self.loc_keeplogin).click()
        self.base.click(self.loc_keeplogin)


    def click_login(self):
        # self.base.find_Element(self.loc_login).click()
        self.base.click(self.loc_login)


    def get_login_username(self):
        try:
            user_name = self.driver.find_element_by_css_selector("#userMenu>a").text
            print(user_name)
            return user_name
        except:
            return ""

    def is_alert(self):
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert()
            text = alert.text
            alert.accept()
            return text
        except:
            return ""

    def forget_passwd(self):
        self.base.click(self.forget_paswd)
        time.sleep(3)
        return self.base.is_text_in_element(self.refresh,"刷新")

    def keep_loginon(self,status=False):
        result = self.base.isSelected(self.loc_keeplogin)
        if status == result:
            pass
        else:
            self.base.click(self.loc_keeplogin)


