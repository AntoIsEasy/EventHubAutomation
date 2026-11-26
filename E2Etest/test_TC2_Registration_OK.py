import pytest
import json
from pathlib import Path

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.Login import LoginPage

data_path = Path(__file__).parent.parent/"Data"/"test_data.json"
with open(data_path) as f:
    test_data = json.load(f) #test data full dictionary
    test_list = test_data["registration"]

@pytest.mark.parametrize("credentials",test_list)

def test_registration_ok(browser_settings,credentials):
    driver = browser_settings
    login_class = LoginPage(driver)
    registration_class = login_class.register_button()

    registration_class.registration_credentials(credentials["New_customer_email"],credentials["New_customer_password"])
    registration_class.create_account_button()
    shown_email = registration_class.get_popup_text()
    assert "@" in shown_email, f"Nessuna mail mostrata in homepage: '{shown_email}'"




