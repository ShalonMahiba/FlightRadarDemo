import pytest

from Config.config import TestData
from Pages.Data import Data
from Pages.Home import Home
from Tests.test_Base import BaseTest


class Test_Data(BaseTest):
    @pytest.mark.sanity
    def test_airport_data(self):
        self.homePage = Home(self.driver)
        self.homePage.consent_page()
        self.homePage.handle_cookie()
        self.driver.maximize_window()
        self.dataPage = Data(self.driver)
        self.dataPage.get_airport_data()

    def test_bhx_search(self):
        self.dataPage = Data(self.driver)
        self.dataPage.search_bhx(TestData.port)


