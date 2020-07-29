class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def loc(self, loc):
        return self.driver.find_element(*loc)

    def quit(self):
        self.driver.quit()