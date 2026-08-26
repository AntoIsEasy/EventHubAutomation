import json
import time
from pathlib import Path

import pytest

from PageObjects.Event import ChooseEvent
from PageObjects.LoginPage import LoginPage
data_path = Path(__file__).parent.parent/"Data"/"test_e2e_ok.json"
with open(data_path) as f:
    test_data = json.load(f) #test data full dictionary
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item",test_list) #insert test_list in test_list_item new brand variable
def test_e2e_shopping(browser_settings,test_list_item):
    #assert variable
    text_confirmation = "Booking Confirmed"

    #TEST

    #setting the driver and login
    driver = browser_settings
    login_class = LoginPage(driver)

    #BrowserUtils call from LoginPage in order to get the get_page_title method
    print(login_class.get_page_title())

    #credentials
    login_class.login_ok(test_list_item["customer_email"],test_list_item["customer_password"])

    #Sign_in and event_page object for ChooseEvent class
    event_page = login_class.sign_in_button()

    # BrowserUtils call from LoginPage in order to get the get_page_title method
    print(event_page.get_page_title())

    #search the event and select it
    selected_event_data = event_page.search_event("Dil")
    #get page title \ compile data form
    print(selected_event_data.get_page_title())
    selected_event_data.setting_credentials(test_list_item["customer_name"],test_list_item["customer_email"],test_list_item["customer_phone_number"])

    #confirm booking
    actual_text = selected_event_data.confirmation()
    assert text_confirmation in actual_text


    time.sleep(3)






