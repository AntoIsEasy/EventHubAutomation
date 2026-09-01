import json
import pytest
from PageObjects.LoginPage import LoginPage
from pathlib import Path

data_path = Path(__file__).parent.parent/"Data"/"test_data.json"
with open(data_path) as f:
    login_data_dict = json.load(f)
    login_data = login_data_dict["login"]

@pytest.mark.parametrize("test_data_list",login_data)
def test_login_ok(browser_settings,test_data_list):
    driver = browser_settings

    login_class = LoginPage(driver)
    login_class.get_page_title()

    login_class.login_form(test_data_list["Customer_email"],test_data_list["Customer_password"])
    login_class.sign_in_button()

    login_class.popup_login()


