from fixture.screen_helper.general_helper import GeneralHelper
from fixture.screen_helper.browser_starter import BrowserHelper
from fixture.screen_helper.first_screen_helper import FirstScreenHelper


class AppManager:

    def __init__(self, var):
        self.var = var
        self.browser = BrowserHelper(self)
        self.general = GeneralHelper(self)
        self.driver = self.browser.run_driver(var)
        self.first = FirstScreenHelper(self)
