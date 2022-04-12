import pytest

from Config.config import TestData
from Pages.Home import Home
from Tests.test_Base import BaseTest


class Test_Home(BaseTest):
    @pytest.mark.regression
    def test_consent_accept(self):
        self.homePage = Home(self.driver)
        self.homePage.consent_page()

    @pytest.mark.regression
    def test_cookie_handle(self):
        self.homePage = Home(self.driver)
        self.homePage.handle_cookie()

    @pytest.mark.sanity
    def test_page_title(self):
        self.homePage = Home(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

