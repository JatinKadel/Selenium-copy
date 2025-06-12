import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    def depart_loc(self, depart_loc):

        self.driver.find_element(By.XPATH, "//p[@title='New Delhi']").click()
        depart_from = self.driver.find_element(By.XPATH, "//input[@id='input-with-icon-adornment']")
        depart_from.click()
        depart_from.send_keys(depart_loc)
        self.driver.find_element(By.XPATH, "(//div[@class='css-36ryd3'])[1]").click()

    def goint_to(self, going_loc):
        self.driver.find_element(By.XPATH, "//p[@title='Mumbai']").click()
        goint_to = self.driver.find_element(By.XPATH, "//input[@id='input-with-icon-adornment']")
        goint_to.click()
        goint_to.send_keys(going_loc)
        time.sleep(2)
        search_result = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']//li")
        for result in search_result:
            if "New York" in result.text:
                result.click()
                break

    def select_date(self, dep_date):
        # Resolve sync issue
        #self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-w7k25o'])[1]"))).click()
        self.wait_until_element_is_clickable(By.XPATH, "(//div[@class='css-w7k25o'])[1]").click()
        # driver.find_element(By.XPATH, "(//div[@class='css-w7k25o'])[1]").click()
        #self.wait.until(EC.element_to_be_clickable((By.XPATH,
                      #                             "//div[contains(@aria-label,'2025-05')]//div[contains(@aria-label,'Choose Friday, May 30th, 2025')]"))).click()
        self.wait_until_element_is_clickable(By.XPATH,"//div[contains(@aria-label,'2025-05')]//div[contains(@aria-label,'Choose Friday, May 30th, 2025')]").click()

        all_dates = self.driver.find_elements(By.XPATH, '//div[@class="react-datepicker__month"]//div[@aria-disabled="false"]')
        for date in all_dates:
            #"Choose Friday, May 30th, 2025"
            if date.get_attribute("aria-label") == dep_date:
                date.click()
            break
    def click_search(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)