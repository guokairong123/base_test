from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Base:
    _driver = None

    def __init__(self, driver: WebDriver = None):
        print("初始化driver")
        if driver is None:
            desired_caps = {'platformName': 'Android',
                            'platformVersion': '6.0',
                            'deviceName': '127.0.0.1:7555',
                            'appPackage': ' com.tencent.wework',
                            'appActivity': '.launch.WwMainActivity',
                            'noReset': 'true',
                            'dontStopAppOnReset': 'true',
                            'unicodeKeyboard': 'true',
                            'resetKeyboard': 'true'
                            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver = driver

    def find(self, locator, value):
        self._driver.find_element(locator, value)