from selenium.webdriver.common.by import By
from Utils.BrowerUtils import Utility


class registration(Utility):
    def __init__(self,driver):
        super().__init__(driver)

        self.email_loc = (By.XPATH,"//input[@id='register-email']")
        self.psw_loc = (By.XPATH,"//input[@id='register-password']")
        self.psw_repeat_loc = (By.XPATH,"//input[@placeholder='Repeat your password']")
        self.button_loc = (By.XPATH,"//button[@id='register-btn']")
        self.popup_loc = (By.XPATH,"//div[@aria-live='polite']//p[normalize-space() = 'Email already registered']")



    def registration_credentials(self,New_customer_email,New_customer_password):
        self.driver.find_element(*self.email_loc).send_keys(New_customer_email)
        self.driver.find_element(*self.psw_loc).send_keys(New_customer_password)
        self.driver.find_element(*self.psw_repeat_loc).send_keys(New_customer_password)


    def create_account_button(self):
        self.driver.find_element(*self.button_loc).click()
