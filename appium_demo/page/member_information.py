from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_demo.page.base import Base


class MemberInformation(Base):
    def delete_member(self):
        self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("删除成员"))').click()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        return self

    def goto_address_list(self):
        locator = (MobileBy.ID, 'com.tencent.wework:id/gvd')
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self._driver.find_element(*locator).click()
        from appium_demo.page.address_list import AddressList
        return AddressList(self._driver)
