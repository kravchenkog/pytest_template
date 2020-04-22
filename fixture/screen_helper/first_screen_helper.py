from selenium.webdriver.common.by import By


class FirstScreenHelper():
    def __init__(self, app):
        self.app = app
        self.general = self.app.general

        self.element = {
            By.CSS_SELECTOR: "div[class^='blabla']"
        }

    def first_method(self):
        pass