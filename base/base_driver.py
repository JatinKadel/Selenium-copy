import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_Scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            lenofPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True

        time.sleep(4)

    def wait_for_presence_of_all_elements(self, loc_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_element = wait.until(EC.presence_of_all_elements_located((loc_type,locator)))
        return  list_of_element

    def wait_until_element_is_clickable(self, loc_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((loc_type,locator)))
        return element