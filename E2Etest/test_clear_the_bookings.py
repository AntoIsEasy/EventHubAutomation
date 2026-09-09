import json
import time

import pytest
from pathlib import Path
from PageObjects.LoginPage import LoginPage

data_path= Path(__file__).parent.parent/ "Data" / "test_data.json"
with open(data_path) as f:
    json_data=json.load(f)
    test_data=json_data["no_seat_available"]


@pytest.mark.parametrize("test_list_item",test_data)
def test_clear_the_bookings(browser_settings,test_list_item):  #COORRREEEEGIIIIII dalle altre parti il nome della def
    driver = browser_settings
    Login_page = LoginPage(driver)
    Login_page.login_form(test_list_item["Customer_email"],test_list_item["Customer_password"])
    event_obj = Login_page.sign_in_button()
    selection_obj = event_obj.my_bookings()
    selection_obj.clear_all_bookings()

    time.sleep(3)
