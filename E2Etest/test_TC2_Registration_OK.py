import pytest
import json
from pathlib import Path
from PageObjects.Login import LoginPage
import uuid
from Utils.BrowerUtils import Utility

data_path = Path(__file__).parent.parent/"Data"/"test_data.json"
with open(data_path) as f:
    test_data = json.load(f) #test data full dictionary
    test_list = test_data["registration"] #this data must be changed manually
    random_values = uuid.uuid4().hex[:8]

@pytest.mark.parametrize("credentials",test_list)
def test_registration_ok(browser_settings,credentials):
    driver = browser_settings
    login_class = LoginPage(driver)
    registration_class = login_class.register_button()

    #add credentials from json file to the registration form
    registration_class.registration_credentials(f"userdemo{random_values}{credentials["New_customer_email"]}",credentials["New_customer_password"])
    registration_class.create_account_button()
    #save the email shown in the homepage, once logged in
    shown_email = registration_class.email_presence_for_logged_user()
    assert "@" in shown_email, f"Nessuna mail mostrata in homepage: '{shown_email}'"
    actual_url = registration_class.get_current_url()
    assert actual_url == "https://eventhub.rahulshettyacademy.com/"





