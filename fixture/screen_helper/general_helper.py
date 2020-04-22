import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class GeneralHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

        '''The element should be presented in the screen, 
        To check presenting (existing) need to use el_is_presented method'''

    def el_is_displayed(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        return el.is_displayed()

    '''The method takes webdriver element'''

    def el_is_displayed_by_el(self, el):
        return el.is_displayed

    '''The method checks is the current url the same as received string
        url = str'''

    def screen_is_presented_by_url(self, url):
        if self.driver.current_url == url:
            return True
        else:
            return False

    '''The method takes locator in next format:
        lc = {By.[type of selector]: selector}/ 'arg' 
        parameter can use for additional selector ]'''

    def but_press(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        self.driver.find_element(locator_type, locator_value).click()

    '''The method takes webdriver element'''

    def but_press_by_el(self, button):
        button.click()

    '''The method returns true if '''
    def el_is_presented(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_elements(locator_type, locator_value)
        return True if el else False

    def get_el_by_text(self, text, elements_list, arg=0):
        text = text.lower()
        locator_type = list(elements_list.keys())[arg]
        locator_value = list(elements_list.values())[arg]
        els = self.driver.find_elements(locator_type, locator_value)
        counter = 0
        try:

            el = [x for x in els if text in x.text.lower()][0]

        except IndexError:
            el = False
        return el

    def find_elS_in_element(self, main_el, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        elements = main_el.find_elements(locator_type, locator_value)
        return elements

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_presence_of_el(self, element, time, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((locator_type, locator_value)))

    def wait_not_presence_of_el(self, element, time, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        WebDriverWait(self.driver, time).until_not(
            EC.presence_of_element_located((locator_type, locator_value)))

    def wait_presence_of_elS(self, element, time, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located((locator_type, locator_value)))

    def wait_clickable_el(self, element, time, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        WebDriverWait(self.driver, time).until_not(
            EC.element_to_be_clickable((locator_type, locator_value)))

    def send_k(self, element, string, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        self.driver.find_element(locator_type, locator_value).send_keys(string)

    def send_key_by_element(self, element, string):
        element.send_keys(string)

    def get_txt_of_el(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        return el.text

    def get_list_of_texts_in_elements(self, elements_list):

        text = [x.text for x in elements_list]
        return text

    def get_text_of_element_by_element(self, el):
        return el.text

    def find_el_and_return(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        return el

    def find_elS_and_return(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_elements(locator_type, locator_value)
        return el

    def fld_clear(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        el.clear()

    def fld_clear_by_el(self, element):
        element.clear()

    def fld_clear_keyboard(self, element, key, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        el.send_keys(key)

    def get_text_of_input(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        return el.get_attribute('value')

    def get_attr_of_element(self, element, attr, arg=0):
        attr = element.get_attribute(attr)
        return attr

    def get_el_by_name(self, name, locator):
        el = self.get_el_by_text(text=name, elements_list=locator)
        return el

    def upload_file(self, el, file):
        p = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../tests/test_data"))
        el.send_keys(p + "/" + file)

    def refresh_current_scr(self):
        self.driver.refresh()

    def hover_and_click(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        hover = ActionChains(self.driver).move_to_element(el)
        hover.click().perform()

    def open_url_in_new_tab(self, url):
        self.driver.execute_script("window.open('https://{}');".format(url))

    def switch_to_frame(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        self.driver.switch_to.frame(self.driver.find_element(locator_type, locator_value))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def execute_script(self, script):
        resp = self.driver.execute_script(script)
        return resp

    def click_key(self, key):
        ActionChains(self.driver).send_keys(key).perform()

    def click_by_coordinates(self, element, x, y):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(
            to_element=element,
            xoffset=x,
            yoffset=y
        )
        action.click()
        action.perform()
