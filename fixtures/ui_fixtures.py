from page_objects.page_object.google_search_page import GoogleSearchPage
from utilities.myselenium_driver import SeleniumDriver


class UI:

    def __init__(self, driver):
        # Initialize all the page object classes below
        self.driver = driver
        self.implicit_wait = self.driver.implicitly_wait(10)
        self.common_helpers = SeleniumDriver(self)
        self.google_search_page = GoogleSearchPage(self)

    # def open(self):
    #     self.driver.get(self.url)

    def destroy(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def close(self):
        self.driver.close()
