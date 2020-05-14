from selenium import webdriver


class WXWrokLogin():
    def setup(self):
        self.driver = webdriver.Chrome()
    def teardown(self):
        pass
    def WXWork_login(self):
