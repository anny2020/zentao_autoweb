# @Time: 2020/3/23  13:26
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
from pykeyboard import PyKeyboard
driver = webdriver.Firefox()
driver.get('http://note.youdao.com/')
# ele1 = WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id("account"))
# print(ele1)
# ele1.send_keys('admin')
# # element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))
# # is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element_by_id("someId").is_displayed())
# ele2 = WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_name("password"))
# ele1.send_keys('123456')
# ele3 = WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id("submit"))
# ele1.click()
print(driver.current_window_handle)
a = driver.find_element_by_id("btn-down").click()
time.sleep(3)
k = PyKeyboard()
k.tap_key(k.tab_key)
k.tap_key(k.enter_key)


