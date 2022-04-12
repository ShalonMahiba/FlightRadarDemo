from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

'''This contains all generic methods and utilities for all pages'''

logging.basicConfig(filename="C:\\Users\\mahib\\PycharmProjects\\FlightRadarDemo\\Logstest.log",
                    format='%(asctime)s: %(levelname)s: %(name)s',
                    datefmt='%m/%d/%y %I:%M:%S %p',
                    )

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("")
logger.info("")
logger.warning("")
logger.error("")
logger.critical("")


class Base:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def perform_move(self, by_locator):
        action = ActionChains(self.driver)
        action.move_to_element(
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))).click().perform()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
