from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Select import Selection
from Utils.BrowerUtils import Utility


class ChooseEvent(Utility):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.search_bar = (By.CSS_SELECTOR,"input[placeholder='Search events, venues…']")
        self.element_located = (By.XPATH, "//h3[text()='Dilli Diwali Mela']")


    def search_event(self,event_input):
        #explore all events
        explore_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Explore All Events']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", explore_button)
        # native click gets intercepted by the footer on wide/maximized viewports
        # (layout overlap on this site), so click via JS instead
        self.driver.execute_script("arguments[0].click();", explore_button)

        #search
        self.driver.find_element(*self.search_bar).send_keys(event_input)

        #book now
        self.driver.find_element(By.XPATH, "//a[@id='book-now-btn']").click()
        select_data = Selection(self.driver)
        return select_data











