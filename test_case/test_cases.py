import pytest
from page_object.login import Login
from init.init import start_app
from common.common import read_excel
from log.log import Logger
data = read_excel('../config/login.xlsx','Sheet1')
class TestCase():
    def setup(self) -> None:
        Logger().log().info("开始执行前置条件setup")#对日志配置文件还不熟，使用的还是原来的日志形式
        Logger().log().info("正在打开app...")
        self.driver = start_app()
        self.lp = Login(self.driver)

    def teardown(self) -> None:
        Logger().log().info("开始执行后置条件teardown")
        Logger().log().info("关闭app")
        self.lp.quit()

    def setup_class(self):
        Logger().log().info("执行类的前置条件setup_class")

    def teardown_class(self):
        Logger().log().info("执行类的后置条件teardown_class")



    #登录
    @pytest.mark.parametrize('username,password', data)
    def test_login01(self,username,password):
        self.lp.login(username, password)
        assert self.lp.assert_txt() == True
        Logger().log().info("--------断言结束--------")

if __name__ == '__main__':
    pytest.main()


