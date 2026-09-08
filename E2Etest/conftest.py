import time

import pytest
from selenium import webdriver

@pytest.fixture()
def browser_settings():

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


