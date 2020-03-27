# @Time: 2020/3/25  21:20
from selenium import webdriver
from common.base import Base
import time
from pykeyboard import PyKeyboard


class Addbug():

    def __init__(self,driver):
        self.driver = driver
        self.base = Base(driver)
        #定位登录
        self.loc_username = ('id','account')
        self.loc_paswd = ("name","password")
        self.loc_login = ("id","submit")
        #定位添加BUG
        self.test_link = ('xpath',".//*[@id='mainmenu']/ul/li[4]/a")
        self.bug_link = ('xpath',".//*[@id='modulemenu']/ul/li[2]/a")
        self.add_bug = ('link text','提Bug')
        self.bug_title = ('id','title')
        self.body = ('class name','article-content')
        self.save = ('id','submit')
        self.version = ('xpath',".//*[@id='openedBuild_chosen']/ul")
        self.trunk = ('xpath',".//*[@id='openedBuild_chosen']/div/ul/li")
        self.buglist = ('xpath',".//*[@id='bugList']/tbody/tr[1]/td[4]/a")
        self.bug_init_title = '测试用例标题'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #用sendkey的方法上传文件的参数
        self.uploadfile = ("class name","fileControl")
        #用pykeyboard方法上传文件的参数 点击操作步骤上的图片按钮，点击后再点击浏览
        self.upload = ("xpath",".//*[@id='dataform']/table/tbody/tr[6]/td/div[2]/div[1]/span[18]/span")
        self.liulan = ("css selector",".ke-inline-block.ke-upload-button")
        self.confirm = ("css selector",".ke-button-common.ke-button-outer.ke-dialog-yes")


#登录
    def login(self):
        self.base.send_Keys(self.loc_username,'admin')
        self.base.send_Keys(self.loc_paswd,'123456')
        self.base.click(self.loc_login)
#点击测试
    def add_the_bug(self):
        self.base.click(self.test_link)
        self.base.click(self.bug_link)
        self.base.click(self.add_bug)
        self.base.click(self.version)
        self.base.click(self.trunk)
        self.base.send_Keys(self.bug_title,self.bug_init_title)
        self.driver.switch_to.frame(1)
        self.base.send_Keys(self.body,'测试步骤')
        self.driver.switch_to.default_content()
        #用pykeyboard方法进行上传文件的操作
        self.base.click(self.upload)
        self.base.click(self.liulan)
        #用sendkey方法进行上传文件的操作
        # self.base.send_Keys(self.uploadfile,"D:\\a.txt")
        time.sleep(3)
        k = PyKeyboard()
        a = "D:\\a.txt"
        for i in a:
            k.tap_key(i)
        time.sleep(2)
        k.tap_key(k.enter_key)
        k.tap_key(k.enter_key)
        self.base.click(self.confirm)
        time.sleep(3)
        self.base.click(self.save)

    def add_bug_success(self):
        return self.base.is_text_in_element(self.buglist,self.bug_init_title)
        # result = self.base.find_Element(self.buglist).text




# if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     driver.get("http://127.0.0.1/zentao/user-login.html")
#     addbug = Addbug(driver)
#     addbug.login()
#     result1 = addbug.add_the_bug()
#     print(result1)










