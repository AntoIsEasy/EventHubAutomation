class Utility:

    def __init__(self,driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
