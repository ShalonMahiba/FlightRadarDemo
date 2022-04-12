from selenium.webdriver.common.by import By

from Pages.Base import Base


class Data(Base):
    data = (By.XPATH, "//a[@id = 'navTopDataHistory']")
    airport = (By.XPATH, "//span[text() = 'Airports']")
    search = (By.XPATH, "//input[@id = 'searchAirport']")
    bhx_airport = (By.XPATH, "//span[@class = 'tt-dropdown-menu']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_airport_data(self):
        self.do_click(self.data)
        self.do_click(self.airport)

    def search_bhx(self, port):
        self.do_send_keys(self.search, port)
        self.perform_move(self.bhx_airport)




