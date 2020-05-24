from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_demo.page.main import Main


class TestWork2:
    def setup_class(self):
        self.main = Main()

    #@pytest.mark.skip
    def test_work2_add(self):
        self.main.goto_address_list().goto_add_member().input_name().select_gender()\
        .input_iphone_num().click_save().goto_address_list()
        # toast = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        # #print(self.driver.page_source)
        # assert toast == '添加成功'

    #@pytest.mark.skip
    def test_work2_delete(self):
        self.main.goto_address_list().set_member().goto_member_information().delete_member()\
            .goto_address_list()