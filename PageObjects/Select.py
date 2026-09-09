from selenium.webdriver.common.by import By
from Utils.BrowerUtils import Utility


class Selection(Utility):
    def __init__(self,driver):
        super().__init__(driver)

        self.driver = driver
        self.add_button = (By.XPATH, "//button[text()='+']")
        self.customer_name_loc = (By.CSS_SELECTOR,"#customerName")
        self.customer_email_loc = (By.ID,"customer-email")
        self.customer_phone_number_loc = (By.ID,"phone")
        self.confirm_button = (By.ID,"confirm-booking")
        self.succesfull_text = (By.XPATH, "//h3[contains(text(),'Booking Confirmed')]")
        self.clear_bookings_loc = (By.XPATH,"//button[text()='Clear all bookings']")
        self.assertion_text = (By.XPATH,"//h3[contains(text(),'yet')]")

    def setting_credentials(self,customer_name,customer_email,customer_phone_number):
        self.driver.find_element(*self.add_button).click()
        self.driver.find_element(*self.customer_name_loc).send_keys(customer_name)
        self.driver.find_element(*self.customer_email_loc).send_keys(customer_email)
        self.driver.find_element(*self.customer_phone_number_loc).send_keys(customer_phone_number)


    def confirmation(self):
        confirm_button = self.driver.find_element(*self.confirm_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", confirm_button)
        self.driver.execute_script("arguments[0].click();", confirm_button)
        Successful_booking = self.driver.find_element(*self.succesfull_text).text
        return Successful_booking

    def clear_all_bookings(self):
        self.driver.find_element(*self.clear_bookings_loc).click()

        #alert management
        alert = self.driver.switch_to.alert
        alert.accept()
        text_no_booking = self.driver.find_element(*self.assertion_text).text
        #assert "no bookings"
        assert 'bookings' in text_no_booking

