from common.common import Common
from selenium.webdriver.common.by import By
from log.log import Logger
from selenium.webdriver.support.ui import WebDriverWait
from page_object.login import Login
class Register(Common):
    uname = (By.ID,'com.tal.kaoyan:id/activity_register_username_edittext')
    upwd = (By.ID,'com.tal.kaoyan:id/activity_register_password_edittext')
    email = (By.ID,'com.tal.kaoyan:id/activity_register_email_edittext')
    regisbt = (By.ID,'com.tal.kaoyan:id/activity_register_register_btn')

    def register(self,username,password,email):
        self.cance()
        self.skip()
        Logger().log().info("开始注册")
        self.loc(Login.regis).click()
        WebDriverWait(self.driver, 5).until(lambda el:el.find_element(*self.uname))
        self.loc(self.uname).send_keys(username)
        self.loc(self.upwd).send_keys(password)
        self.loc(self.email).send_keys(email)
        self.loc(self.regisbt).click()
        Logger().log().info("注册完成")

    def assert_txt(self):
        msg = "注册成功"
        message = '//*[@text=\'{}\']'.format(msg)
        try:
            toast_element = WebDriverWait(self.driver, 5).until(lambda el: el.find_element_by_xpath(message))
            Logger().log().info("断言成功，找到断言元素，元素的text属性为：{}".format(toast_element.text))
            return True
        except:
            Logger().log().info("断言失败，未找到断言元素")
            return False
