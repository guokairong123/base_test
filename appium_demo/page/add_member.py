from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_demo.page.base import Base


class AddMember(Base):

    def input_name(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='姓名　']/../*[@class='android.widget.EditText']").send_keys(
            "测试")
        return self

    def select_gender(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='性别']/../*[@class='android.widget.RelativeLayout']").click()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        return self

    def input_iphone_num(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys("17866535412")
        return self

    def click_save(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gvk']").click()
        return self

    def goto_address_list(self):
        locator = (MobileBy.ID, 'com.tencent.wework:id/gv3')
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self._driver.find_element(*locator).click()
        from appium_demo.page.address_list import AddressList
        return AddressList(self._driver)
