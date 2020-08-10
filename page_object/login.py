from base_page.base_page import BasePage
from init.init import start_app
from common.common import Common
from selenium.webdriver.common.by import By
from log.log import Logger
from selenium.webdriver.support.ui import WebDriverWait
class Login(Common):
    uname = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    upwd = (By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginbt = (By.ID,'com.tal.kaoyan:id/login_login_btn')
    regis = (By.ID,'com.tal.kaoyan:id/login_register_text')

    def login(self,username,password):
        self.cance()
        self.skip()
        # driver = start_app()
        # Common(driver).cance()
        # Common(driver).skip()
        Logger().log().info("开始登录")
        self.loc(self.uname).send_keys(username)
        self.loc(self.upwd).send_keys(password)
        self.loc(self.loginbt).click()
        Logger().log().info("结束登录")

    def assert_txt(self):
        error_message = "用户名或密码错误，你还可以尝试1次"
        limit_message = "验证失败次数过多，请15分钟后再试"

        message = '//*[@text=\'{}\']'.format(limit_message)
        # message='//*[@text=\'{}\']'.format(limit_message)
        # 显示等待lambda匿名函数，如果获取不到会超时报错
        try:
            toast_element = WebDriverWait(self.driver, 5).until(lambda el: el.find_element_by_xpath(message))
            Logger().log().info("断言成功，找到断言元素，元素的text属性为：{}".format(toast_element.text))
            return True
        except:
            Logger().log().info("断言失败，未找到断言元素")
            return False

if __name__ == '__main__':
    driver = start_app()
    lp = Login(driver)
    lp.login('小可爱', 'trr123456')

