import os
from selenium import webdriver
import datetime


class BrowserHelper():
    def __init__(self, app):
        self.app = app

    def get_desired_cup(self, var):
        desired_cap = {
            "browserName": var['browser'],
            "platform": "Linux",
            "name": "{} report test {}".format(var['test_name'],
                                               datetime.datetime.now()),
            "timeout": 100,
            'resolution': '1920x1080'
        }
        return desired_cap

    def run_driver(self, var):
        desired_cap = self.get_desired_cup(var)
        if var['local'] == 1:
            path = os.path.dirname(os.path.abspath(__file__))
            path = path + "/../chromedriver"
            driver = webdriver.Chrome(executable_path=path)
        else:
            print("REALIZED LOCAL RUN ONLY")

        # ZALENIUM RUNNER
        # elif variables['env'] == "prod":
        #
        #     driver = webdriver.Remote(
        #         command_executor="http://zalenium-prod-eu-west-1.mes.glomex.cloud/wd/hub",
        #         desired_capabilities=desired_cap)
        # else:
        #
        #     driver = webdriver.Remote(
        #         command_executor="http://zalenium-stage-eu-west-1.stage.mes.glomex.cloud/wd/hub",
        #         desired_capabilities=desired_cap)

        driver.implicitly_wait(5)

        if var['env'] == 'prod':
            driver.get(self.app.h_env.base_url)
        return driver

    def mark_build(self, status):
        if status:
            self.app.driver.add_cookie({'name': 'zaleniumTestPassed',
                                        'value': "false"})
        else:
            self.app.driver.add_cookie({'name': 'zaleniumTestPassed',
                                        'value': "true"})
