from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.Base import Base


class Home(Base):
    consent = (By.XPATH, '//*[@id="map"]/div[15]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    cookie = (By.XPATH, "//button[text()='Accept Cookies']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def consent_page(self):
        self.do_click(self.consent)

    def handle_cookie(self):
        self.do_click(self.cookie)

