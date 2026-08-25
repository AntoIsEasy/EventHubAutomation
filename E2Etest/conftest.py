import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser_settings():
    chrome_service = Service("C:/Users/lapto/Desktop/ChromeDriver/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()


