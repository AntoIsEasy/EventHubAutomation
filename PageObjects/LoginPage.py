from selenium.webdriver.common.by import By

from PageObjects.Event import ChooseEvent
from Utils.BrowerUtils import Utility


#va aggiunto openpxl (vedi excel.py) per prendere l'utente dal foglio excel

class LoginPage(Utility):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.email_locator = (By.ID,"email")
        self.password_locator = (By.ID,"password")
        self.login_button_locator = (By.CSS_SELECTOR,"#login-btn")



    def login_ok(self,user_email,user_password):
        self.driver.get("https://eventhub.rahulshettyacademy.com/login")
        #credentials
        self.driver.find_element(*self.email_locator).send_keys(user_email)
        self.driver.find_element(*self.password_locator).send_keys(user_password)

    def sign_in_button(self):
        #sign in button
        self.driver.find_element(*self.login_button_locator).click()
        event_page = ChooseEvent(self.driver)
        return event_page



