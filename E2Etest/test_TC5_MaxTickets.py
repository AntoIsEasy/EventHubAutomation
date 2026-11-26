from pathlib import Path
import json
from PageObjects.Login import LoginPage
import pytest
from ApiUtils.ApiUtils import UtilsAPI

data_path = Path(__file__).parent.parent/"Data"/"test_data.json"
with open(data_path) as f:
    test_data = json.load(f)
    list_data = test_data["max_min_ticket"]

@pytest.mark.ui
@pytest.mark.parametrize("list_data_users",list_data)
def test_max_ticket(browser_settings,list_data_users):
    driver = browser_settings

    #obj Login, form and submit button
    Login_form = LoginPage(driver)
    Login_form.login_form(list_data_users["Customer_email"],list_data_users["Customer_password"])
    event_selection = Login_form.sign_in_button()

    #find book now on available event
    select_page = event_selection.book_now()

    #API calls to retrieve the value of the availableSeats (max number of tickets)
    Api_calls = UtilsAPI()
    get_token = Api_calls.get_token(list_data_users["Customer_email"],list_data_users["Customer_password"])
    availableSeats = Api_calls.get_ticket_numbers(get_token)

    actual_seats_booked = select_page.max_ticket_buttons()

    #check if the user has clicked 10 times
    assert int(actual_seats_booked) == availableSeats


