from utilities.myselenium_driver import SeleniumDriver


class DummyPage(SeleniumDriver):

    def __init__(self, ui):
        super().__init__(ui)
        self.driver = ui.driver

    def get_page_title(self):
        try:
            print("PAGE TITLE: ", self.get_title())
        except Exception:
            raise
