import pytest
import time
from Config.config import TestData
from Pages.Departures import Departures
from Pages.Home import Home
from Pages.Data import Data
from Tests.test_Base import BaseTest


class Test_Departures(BaseTest):
    def test_airport_data(self):
        self.homePage = Home(self.driver)
        self.homePage.consent_page()
        self.homePage.handle_cookie()
        self.driver.maximize_window()
        self.dataPage = Data(self.driver)
        self.dataPage.get_airport_data()
        self.dataPage.search_bhx(TestData.port)
        self.depPage = Departures(self.driver)
        self.depPage.go_to_dep()
