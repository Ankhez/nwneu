from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from MessagesLocator import MessagesPageLocators


class Base(object):

    def __init__(self, driver):
        self.driver = driver


class BasicAction(Base):
    class_description = "Basic Action for Elements"

    def click(self, locator):
        click_on_login_button = self.driver.find_element(*locator)
        click_on_login_button.click()

    def input_box(self, locator, text):
        input_in_form_login = self.driver.find_element(*locator)
        input_in_form_login.send_keys(text)

    def get_count_of_element(self, locator):
        size = self.driver.find_elements(*locator)
        size = size.__len__()
        return size

    def check_exists_by_locator(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def get_text_from_element(self, locator):
        if self.check_exists_by_locator(locator) is True:
            size = self.get_count_of_element(locator)
            values = []
            while size != 0:
                sizetostr = size.__str__()
                name = self.driver.find_element_by_xpath(locator[1]+"["+sizetostr+"]").text
                size -= 1
                values.append(name)
            return values

