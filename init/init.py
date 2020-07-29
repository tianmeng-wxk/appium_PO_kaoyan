import yaml
from appium import webdriver

def start_app():
    with open('../init/init_conf.yaml', 'r', encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)  # 或者yaml.full_load()
    cas = {}
    cas['platformName'] = yaml_data['platformName']
    cas['platformVersion'] = yaml_data['platformVersion']
    cas['deviceName'] = yaml_data['deviceName']
    cas['app'] = yaml_data['app']
    cas['appPackage'] = yaml_data['appPackage']
    cas['appActivity'] = yaml_data['appActivity']
    cas['noReset'] = yaml_data['noReset']
    cas['unicodeKeyboard'] = yaml_data['unicodeKeyboard']
    cas['resetKeyboard'] = yaml_data['resetKeyboard']
    driver = webdriver.Remote('http://' + str(yaml_data["ip"]) + ':' + str(yaml_data["port"]) + '/wd/hub', cas)
    driver.implicitly_wait(5)
    return driver