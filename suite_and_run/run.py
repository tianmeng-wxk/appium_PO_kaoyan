import pytest,os,time,sys
#添加路径
path = 'E:\\script\\appium_PO_kaoyan'
sys.path.append(path)
from common.common import send_email,send_mail

if __name__ == '__main__':
    #生成pytest-html报告
    report_path = "../report/"
    report_file = report_path+"{}_pytest_html_report.html".format(time.strftime("%Y_%m_%d  %H-%M-%S",time.localtime()))
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    else:
        pass
    pytest.main(["-s", "-v", "../test_case/test_cases.py", "--html="+report_file])
    #发送邮件
    send_mail(report_file)

    #生成allure报告
    # import os
    # pytest.main(['-s','-q','../test_case/test_cases.py','--alluredir=../report/allure_xml'])#生成alure缓存文件
    # os.system('allure generate --clean ../report/allure_xml/ -o ../report/allure_html')
    #os.system('allure serve ../report/allure_xml')