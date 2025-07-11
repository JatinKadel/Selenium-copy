import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    #wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    #request.cls.wait = wait
    yield
    driver.close()