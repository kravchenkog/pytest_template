from fixture.screen_helper.general_helper import GeneralHelper
from fixture.screen_helper.browser_starter import BrowserHelper
from fixture.screen_helper.first_screen_helper import FirstScreenHelper
from fixture.env import Environment


class AppManager:

    def __init__(self, var):
        self.var = var
        self.env = Environment(var)
        self.browser = BrowserHelper(self)
        self.driver = self.browser.run_driver(var)
        self.general = GeneralHelper(self)
        self.first = FirstScreenHelper(self)
        self.env = Environment(var)
