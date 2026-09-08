import time

import pytest
from selenium import webdriver

@pytest.fixture()
def browser_settings():

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.set_window_size(1920,1080)
    yield driver
    driver.quit()


