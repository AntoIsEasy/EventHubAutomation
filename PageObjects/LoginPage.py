import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Event import ChooseEvent
from Utils.BrowerUtils import Utility


class LoginPage(Utility):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.email_locator = (By.ID,"email")
        self.password_locator = (By.ID,"password")
        self.login_button_locator = (By.CSS_SELECTOR,"#login-btn")
        self.error_popup_locator = (By.CSS_SELECTOR,"div[aria-live='polite']")
        self.popup_loc = (By.XPATH, "//p[text()='Invalid email or password']")



    def login_form(self,user_email,user_password):
        self.driver.get("https://eventhub.rahulshettyacademy.com/login")
        #credentials
        self.driver.find_element(*self.email_locator).send_keys(user_email)
        self.driver.find_element(*self.password_locator).send_keys(user_password)


    def sign_in_button(self):
        #sign in button
        self.driver.find_element(*self.login_button_locator).click()
        event_page = ChooseEvent(self.driver)
        return event_page

    def popup_login(self):
        try:  #try block status is passed when the Login is KO and the alert popup is shown
            WebDriverWait(self.driver,3).until(EC.text_to_be_present_in_element(self.popup_loc,"email or password"))
            popup_text = self.driver.find_element(*self.popup_loc).text
            assert  "email or password" in popup_text, f"Unexpected popup text:{popup_text}"

        except TimeoutException: #except block status is passed when the login is OK (first use case)

            page_title = self.get_current_url()
            assert page_title == "https://eventhub.rahulshettyacademy.com/"








