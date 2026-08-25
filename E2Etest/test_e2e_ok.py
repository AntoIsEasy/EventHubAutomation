import time

from PageObjects.Event import ChooseEvent
from PageObjects.LoginPage import LoginPage


def test_e2e_shopping(browser_settings):
    #data for Select.py
    customer_name = "userDemo2"
    customer_email = "demo2@yopmail.com"
    customer_phone_number = "+313331234567"

    #assert
    text_confirmation = "Booking Confirmed"

    #setting the driver and login
    driver = browser_settings
    login_class = LoginPage(driver)

    #BrowserUtils call from LoginPage in order to get the get_page_title method
    print(login_class.get_page_title())

    #credentials
    login_class.login_ok("demo2@yopmail.com","Userdemo2!")

    #Sign_in and event_page object for ChooseEvent class
    event_page = login_class.sign_in_button()

    # BrowserUtils call from LoginPage in order to get the get_page_title method
    print(event_page.get_page_title())

    #search the event and select it
    selected_event_data = event_page.search_event("Dil")
    #get page title \ compile data form
    print(selected_event_data.get_page_title())
    selected_event_data.setting_credentials(customer_name,customer_email,customer_phone_number)

    #confirm booking
    actual_text = selected_event_data.confirmation()
    assert text_confirmation in actual_text


    time.sleep(3)






