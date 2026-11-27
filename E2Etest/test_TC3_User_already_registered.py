from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Registration import registration
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Login import LoginPage
from pathlib import Path
import json
import pytest


Data_path = Path(__file__).parent.parent/"Data"/"test_data.json"
with open(Data_path) as f:
    list_test_data = json.load(f)
    test_data = list_test_data["User_registered"]

@pytest.mark.parametrize("user_credentials",test_data)
def test_user_already_registered(browser_settings,user_credentials):
    driver = browser_settings

    login_class = LoginPage(driver)
    #go on the registration page and insert any already registered user credentials
    get_registration_page = login_class.register_button()
    get_registration_page.registration_credentials(user_credentials["already_registered_email"],user_credentials["already_registered_pqassword"])

    #click on the register button
    get_registration_page.create_account_button()

    #explicit wait on the "alredy regstered" popup
    popup = WebDriverWait(driver,10).until(EC.visibility_of_element_located(get_registration_page.popup_loc)).text

    assert "Email already registered" in popup, f"Il popup non è stato mostrato o il testo'{popup}' non compare"
