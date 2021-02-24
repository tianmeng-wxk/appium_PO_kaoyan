import pytest
from page_object.login import Login
from page_object.register import Register
from init.init import start_app
from common.common import excelData
from log.log import Logger
login_data = excelData().excel_data('../config/login.xlsx', 'Sheet1')
register_data = excelData().excel_data('../config/register.xlsx', 'Sheet1')


class TestCase():
    def setup(self) -> None:
        Logger().log().info("开始执行前置条件setup")#对日志配置文件还不熟，使用的还是原来的日志形式
        Logger().log().info("正在打开app...")
        self.driver = start_app()
        self.driver.implicitly_wait(10)
        self.lp = Login(self.driver)
        self.rp = Register(self.driver)

    def teardown(self) -> None:
        Logger().log().info("开始执行后置条件teardown")
        Logger().log().info("关闭app")
        self.lp.quit()

    def setup_class(self):
        pass

    def teardown_class(self):
        Logger().log().info("-------测试完成-------")

    #登录
    @pytest.mark.smoke
    @pytest.mark.parametrize('username,password', login_data)
    def test_1_login(self, username, password):
        self.lp.login(username, password)
        assert self.lp.assert_txt() == True
        Logger().log().info("--------断言结束--------")

    #注册
    @pytest.mark.parametrize('username,password,email', register_data)
    def test_2_register(self, username, password, email):
        self.rp.register(username, password, email)
        assert self.rp.assert_txt() == True
        Logger().log().info("--------断言结束--------")

if __name__ == '__main__':
    pytest.main()


