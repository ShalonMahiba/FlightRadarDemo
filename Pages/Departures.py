import time
from selenium.webdriver.common.by import By
from Pages.Data import Data


class Departures(Data):
    departures = (By.XPATH, "//a[contains(@class, 'btn ') and text() = ' Departures ']")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_dep(self):
        self.do_click(self.departures)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

