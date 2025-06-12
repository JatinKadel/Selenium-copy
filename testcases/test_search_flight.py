import time

import pytest
from selenium.webdriver.common.by import By
from pages.search_flight_result_page import SearchFlightResult
from pages.yatra_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class Test_yatra():
    def test_search(self):
        # driver = self.driver
        # wait = self.wait

        # Launch Web
        # From location
        lp = LaunchPage(self.driver)
        lp.depart_loc("New Delhi")

        #to location
        lp.goint_to("New York")

        #Resolve sync issue
        #Select date
        lp.select_date("Choose Sunday, June 8th, 2025")

        #click on search flight
        lp.click_search()

        time.sleep(5)
        #To handle dynamic scroll
        lp.page_Scroll()


        # selecting filter
        sf = SearchFlightResult(self.driver)
        sf.filter_flight()


        # all_stops1 = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
        #                                                                   "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))
        all_stops1 = lp.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        print(len(all_stops1))

        #Verify the filtered result
        for stop in all_stops1:
            print("he test is "+stop.text)
            assert stop.text == "1 Stop"
            print("assert pass")


# check = Test_yatra()
# check.test_search()