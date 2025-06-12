import time
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class SearchFlightResult(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver
        # self. wait = wait
    def filter_flight(self):
        self.driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()
        time.sleep(2)
