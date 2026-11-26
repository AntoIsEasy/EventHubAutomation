import json
from pathlib import Path
from ApiUtils.ApiUtils import UtilsAPI
import pytest

from PageObjects.Login import LoginPage
data_path = Path(__file__).parent.parent/"Data"/"test_data.json"
with open(data_path) as f:
    test_data = json.load(f) #test data full dictionary
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item",test_list) #insert test_list in test_list_item new brand variable
def test_validation_rules_in_booking_form(browser_settings,test_list_item):

    #Register a new user through API and save user_mail and password in the credential_list (it is a list)
    api_class = UtilsAPI()
    credential_list = api_class.register_new_user()

    #TEST

    #setting a new name for the driver
    driver = browser_settings

    #login with the credentials created by the previous API call with the
    login_page = LoginPage(driver)
    login_page.login_form(credential_list[0],credential_list[1])
    #Apply POM to return the Event page class
    event_page = login_page.sign_in_button()
    #book any event (it picks up the first event of the page)
    select_class = event_page.book_now()

    #compile data form
    select_class.setting_credentials(test_list_item["customer_name"],test_list_item["customer_email"],test_list_item["customer_phone_number"])

    #confirm booking button and validation text, as a list

    list_of_errors = select_class.confirmation_button_KO()
    assert "Name must be at least 2 chars" in list_of_errors[0]
    assert "Enter a valid email" in list_of_errors[1]
    assert "Enter a valid 10-digit phone" in list_of_errors[2]










