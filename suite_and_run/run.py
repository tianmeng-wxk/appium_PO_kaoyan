import pytest

if __name__ == '__main__':
    #生成pytest-html报告
    #pytest.main(["-s", "-vv", "../test_case/test_cases.py", "--html=../report/pytest_report.html"])

    #生成allure报告
    import os
    pytest.main(['-s','-q','../test_case/test_cases.py','--alluredir=../report/allure_xml'])#生成alure缓存文件
    os.system('allure generate --clean ../report/allure_xml/ -o ../report/allure_html')
    #os.system('allure serve ../report/allure_xml')