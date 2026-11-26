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
        self.confirm_button_loc = (By.ID,"confirm-booking")
        self.succesfull_text = (By.XPATH, "//h3[contains(text(),'Booking Confirmed')]")
        self.clear_bookings_loc = (By.XPATH,"//button[text()='Clear all bookings']")
        self.assertion_text = (By.XPATH,"//h3[contains(text(),'yet')]")
        self.ticket_count_loc = (By.ID,"ticket-count")

        #variables for form validation rules, in the confirmation_button_KO class method
        self.invalid_name_loc = (By.XPATH,"//p[text()='Name must be at least 2 chars']")
        self.invalid_email_loc = (By.XPATH,"//p[text()='Enter a valid email']")
        self.invalid_phone_number_loc = (By.XPATH, "//p[text()='Enter a valid 10-digit phone']")



    def setting_credentials(self,customer_name,customer_email,customer_phone_number):

        self.driver.find_element(*self.customer_name_loc).send_keys(customer_name)
        self.driver.find_element(*self.customer_email_loc).send_keys(customer_email)
        self.driver.find_element(*self.customer_phone_number_loc).send_keys(customer_phone_number)

    def max_ticket_buttons(self):

        while self.driver.find_element(*self.add_button).is_enabled():
            self.driver.find_element(*self.add_button).click()

        ticket_count = self.driver.find_element(*self.ticket_count_loc).text
        return ticket_count



    def confirmation_ok(self):
        confirm_button = self.driver.find_element(*self.confirm_button_loc)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", confirm_button)
        self.driver.execute_script("arguments[0].click();", confirm_button)
        successful_booking = self.driver.find_element(*self.succesfull_text).text
        return successful_booking

    def confirmation_button_KO(self):
        self.driver.find_element(*self.confirm_button_loc).click()
        invalid_name = self.driver.find_element(*self.invalid_name_loc).text
        invalid_email = self.driver.find_element(*self.invalid_email_loc).text
        invalid_phone_number = self.driver.find_element(*self.invalid_phone_number_loc).text

        #I insert the text in a list, in order to send it to test
        list = []
        list.append(invalid_name)
        list.append(invalid_email)
        list.append(invalid_phone_number)
        return list



    def clear_all_bookings(self):
        self.driver.find_element(*self.clear_bookings_loc).click()

        #alert management
        alert = self.driver.switch_to.alert
        alert.accept()
        text_no_booking = self.driver.find_element(*self.assertion_text).text
        return text_no_booking






