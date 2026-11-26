from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.BrowerUtils import Utility


class registration(Utility):
    def __init__(self,driver):
        super().__init__(driver)

        self.email_loc = (By.XPATH,"//input[@id='register-email']")
        self.psw_loc = (By.XPATH,"//input[@id='register-password']")
        self.psw_repeat_password_loc = (By.XPATH,"//input[@placeholder='Repeat your password']")
        self.button_loc = (By.XPATH,"//button[@id='register-btn']")
        self.popup_loc = (By.XPATH,"//div[@aria-live='polite']//p[normalize-space() = 'Email already registered']")
        self.email_present_as_logged_in_loc = (By.XPATH,"//span[@data-testid='user-email-display']")



    def registration_credentials(self,New_customer_email,New_customer_password):
        self.driver.find_element(*self.email_loc).send_keys(New_customer_email)
        self.driver.find_element(*self.psw_loc).send_keys(New_customer_password)
        self.driver.find_element(*self.psw_repeat_password_loc).send_keys(New_customer_password)


    def create_account_button(self):
        self.driver.find_element(*self.button_loc).click()

    def email_presence_for_logged_user(self):
        shown_email = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_present_as_logged_in_loc)).text
        return shown_email
