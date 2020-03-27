# @Time: 2020/3/23  14:52
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
# driver = webdriver.Firefox()
# driver.get("http://127.0.0.1/zentao/user-login.html")
class Base():

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def find_Element2(self,locator):
        ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return ele

    def find_Element(self,locator):
        ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda a: a.find_element(*locator))
        return ele

    def find_Elements(self,locator):
        eles = WebDriverWait(self.driver,self.timeout,self.t).until(lambda a: a.find_elements((locator)))
        return eles

    def send_Keys(self,locator,text):
        ele = self.find_Element(locator)
        ele.send_keys(text)
        time.sleep(3)

    def click(self,locator):
        ele = self.find_Element(locator)
        ele.click()

    def clear(self,locator):
        ele = self.find_Element(locator)
        ele.clear()

    def isSelected(self,locator):
        ele = self.find_Element(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self,locator):
        try:
            ele = self.find_Element(locator)
            return True
        except:
            return False

    def isElementExist2(self,locator):
        try:
            eles = self.find_Elements(locator)
            return eles
        except:
            return []

    def is_title(self,title):
        "判断title是否期望的title"
        try:
            eles = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(title))
            return eles
        except:
            return False

    def is_title_contains(self,title):
        try:
            eles = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(title))
            return eles
        except:
            return False

    def is_text_in_element(self,locator,text):
        try:
            eles = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,text))
            return eles
        except:
            return False

    def is_element_exist3(self,locator):
        try:
            eles = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def is_value_in_element(self,locator,text):
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,text))
            return True
        except:
            return False

    def is_alart_present(self):
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            print(ele.text)
            return ele
        except:
            return False
#鼠标悬停事件
    def move_to_element(self,locator):
        ele = self.find_Element(locator)
        ActionChains(driver).move_to_element(ele).perform()

#select方法  按value选择
    def select_by_value(self,locator,value):
        ele = self.find_Element(locator)
        Select(ele).select_by_value(value)
        ele.click()
#select方法  按index选择
    def select_by_index(self,locator,index):
        ele = self.find_Element()
        Select(ele).select_by_index(index)
        ele.click()

    def select_by_text(self,locator,text):
        ele = self.find_Element(locator)
        Select(ele).select_by_visible_text(text)
        ele.click()

#滚动条操作--滚动到底部
    def scroll_to_bottom(self):
        js = "window.scrollTo(0,document.body.scrollHeight)" #js函数计算了屏幕的高度
        self.driver.execute_script(js)

#滚动条操作--滚动到顶部
    def scroll_to_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

#滚动条操作--滚动到元素出现的位置

    def scroll_to_focus(self,locator):
        target = self.find_Element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)



if __name__ == '__main__':
    driver = webdriver.Firefox()
    base = Base(driver)
    driver.get("https://www.cnblogs.com/yoyoketang/")
    # driver.find_element_by_id("account").send_keys('admin')
    # driver.find_element_by_name('password').send_keys('1234567')
    # driver.find_element_by_id('submit').click()
    # loc = ("link text","设置")
    # loc1 = ("link text","搜索设置")
    loc2 = ("link text","2020年3月24日")
    # base.move_to_element(loc)
    # base.click(loc1)
    # base.select_by_text(loc2,"每页显示50条")
    # base.scroll_to_bottom()
    # time.sleep(2)
    base.scroll_to_focus(loc2)









