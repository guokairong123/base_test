from appium.webdriver.common.mobileby import MobileBy

from appium_demo.page.base import Base


class AddressList(Base):
    def goto_add_member(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self._driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from appium_demo.page.add_member import AddMember
        return AddMember(self._driver)

    def set_member(self):
        self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gvi').click()
        return self

    def goto_member_information(self):
        self._driver.find_element(MobileBy.XPATH,
                                 "//*[@text='测试']/../../../..//*[@resource-id='com.tencent.wework:id/fdh']").click()
        from appium_demo.page.member_information import MemberInformation
        return MemberInformation(self._driver)