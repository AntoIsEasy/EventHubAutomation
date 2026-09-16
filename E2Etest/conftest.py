import time

import pytest
import pytest_html
from selenium import webdriver

@pytest.fixture()
def browser_settings():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.set_window_size(1920,1080)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser_settings")
        if driver:
            screenshot = driver.get_screenshot_as_base64()
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(screenshot, mime_type="image/png"))
            report.extra = extra


