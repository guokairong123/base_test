from appium.webdriver.common.mobileby import MobileBy

from appium_demo.page.address_list import AddressList
from appium_demo.page.base import Base


class Main(Base):
    def goto_address_list(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressList(self._driver)