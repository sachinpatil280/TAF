import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import time


class SeleniumDriver:

    def __init__(self, ui):
        self.driver = ui.driver

    def get_title(self):
        return self.driver.title

    @staticmethod
    def get_by_type(locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            pytest.fail(f"Locator type {locator_type} not correct/supported")

    def get_element(self, locator, locator_type="id"):
        by_type = self.get_by_type(locator_type)
        element = self.driver.find_element(by_type, locator)
        return element

    def get_elements_list(self, locator, locator_type="id"):
        locator_type = locator_type.lower()
        by_type = self.get_by_type(locator_type)
        elementList = self.driver.find_elements(by_type, locator)
        return elementList

    def is_element_checked(self, element=None, locator=None, locator_type="id"):
        status = True
        if element:
            if not element.is_selected():
                status = False
        elif locator:
            if not self.get_element(locator, locator_type).is_selected():
                status = False
        return status

    def click_element(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        self.wait_for_element_to_be_visible(locator, locator_type)
        element.click()

    def click_element_using_actions_class(self, element=None, locator=None, locator_type="id"):
        if element is None:
            element = self.get_element(locator, locator_type)
            self.wait_for_element_to_be_visible(locator, locator_type)
            ActionChains(self.driver).move_to_element(element).click().perform()
        else:
            ActionChains(self.driver).move_to_element(element).click().perform()

    def send_keys(self, data, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        element.send_keys(data)

    def clear_element(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        if len(element.get_attribute("value")) > 0:
            element.clear()

    def remove_attribute(self, locator, attribute):
        self.driver.execute_script(f'document.getElementById("{locator}").removeAttribute("{attribute}")')

    def is_element_present(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        if element is not None:
            return True
        else:
            return False

    def is_element_not_present(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        if element is not None:
            return False
        else:
            return True

    def element_presence_check(self, locator, by_type):
        element_list = self.driver.find_elements(by_type, locator)
        if len(element_list) > 0:
            return True
        else:
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=20, pollFrequency=0.5):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(ec.element_to_be_clickable((by_type, locator)))

        return element

    def wait_for_element_to_be_visible(self, locator, locator_type="id",
                                       timeout=20, pollFrequency=0.5):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(ec.visibility_of_element_located((by_type, locator)))

        return element

    def wait_for_element_to_be_invisible(self, locator, locator_type="id", timeout=20, pollFrequency=0.5):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                             ignored_exceptions=[])
        element = wait.until(ec.invisibility_of_element((by_type, locator)))

        return element

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(2)

    def element_has_text(self, data, locator, locator_type="id"):
        element = self.get_element(locator, locator_type).get_attribute('value')
        if element == data:
            return True
        else:
            return False

    def loading(self):
        attempt = 0
        status = None
        while not status and attempt < 10:
            time.sleep(1)
            status = self.get_element("loading").value_of_css_property('display') == 'none'
            attempt += 1

    def is_element_disabled(self, locator, locator_type):
        attribute = self.get_element(locator, locator_type).get_attribute('disabled')
        if attribute:
            return True
        else:
            return False

    def is_element_enabled(self, locator, locator_type):
        attribute = self.get_element(locator, locator_type).is_enabled()
        if attribute:
            return True
        else:
            return False

    def get_text(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type).text
        return element

    def verify_text(self, data, locator, locator_type="id"):
        element = self.get_element(locator, locator_type).text
        if element == data:
            return True
        else:
            return False

    def get_column_count(self, locator, locator_type="id"):
        element_list = self.get_elements_list(locator, locator_type)
        return len(element_list)

    def element_contains_text(self, data, locator, locator_type="id"):
        element = self.get_element(locator, locator_type).get_attribute('value')
        if element.find(data):
            return True
        else:
            return False

    def context_click(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        self.wait_for_element_to_be_visible(locator, locator_type)
        ActionChains(self.driver).context_click(element).click().perform()

    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        child_window = ''
        for handle in self.driver.window_handles:
            if handle != main_window:
                child_window = handle
                break
        self.driver.switch_to.window(child_window)

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_attribute(self, attributeValue, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        attribute = element.get_attribute(attributeValue)
        return attribute

    def switch_to_frame(self, element_id):
        self.driver.switch_to.frame(element_id)

    def get_css_value(self, cssValue, locator, locator_type="id"):
        """
        :param cssValue: The CSS value which we want to retrieve (eg: color, font)
        :param locator: The Web Element on which action needs to be taken.
        :param locator_type: xpath, id etc.
        """
        element = self.get_element(locator, locator_type)
        return element.value_of_css_property(cssValue)

    def get_element_text_using_dom(self, element, element_type='class'):
        """
        Used to extract test from DOM by using Element Type as Class or ID
        :param element: Class Name or ID value
        :param element_type:class or id
        :return: List of text values
        """
        text_list = []
        if element_type == 'class':
            ele_list_length = self.driver.execute_script(
                'return document.querySelectorAll(".' + element + '").length')
            for i in range(ele_list_length):
                val = 'return document.querySelectorAll(".' + element + '")[' + str(i) + '].value'
                text_value = self.driver.execute_script(val)
                text_list.append(text_value)
            return text_list
        elif element_type == 'id':
            ele_list_length = self.driver.execute_script(
                'return document.querySelectorAll("#' + element + '").length')
            for i in range(ele_list_length):
                val = 'return document.querySelectorAll("#' + element + '")[' + str(i) + '].value'
                text_value = self.driver.execute_script(val)
                text_list.append(text_value)
            return text_list

    def click_element_using_dom(self, element):
        """
         Used to extract test from DOM by using Element Type as Class or ID
         :param element: Class Name or ID value
         :return: List of text values
        """
        val = f'return document.querySelector("{element}").click();'
        self.driver.execute_script(val)

    def wait_for_element_to_be_present(self, locator, locator_type="xpath", timer=10):
        by_type = self.get_by_type(locator_type)
        element = WebDriverWait(self.driver, timer).until(ec.presence_of_element_located((by_type, locator)))
        return element

    def wait_for_frame_to_be_available_and_switch_to_it(self, locator, locator_type="xpath", timer=120):
        by_type = self.get_by_type(locator_type)
        element = WebDriverWait(self.driver, timer).until(ec.frame_to_be_available_and_switch_to_it((by_type, locator)))
        return element

    def wait_for_text_to_be_present_in_element(self, text, locator, locator_type="xpath", timer=10):
        by_type = self.get_by_type(locator_type)
        element = WebDriverWait(self.driver, timer).until(ec.text_to_be_present_in_element((by_type, locator), text))
        return element
