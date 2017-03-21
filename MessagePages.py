# -*- coding: utf-8 -*-
from MainPageLocators import MainPageLocators
from MessagesLocator import MessagesPageLocators, MesssagesReaction
from JSONPROCESS import JSONDate
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import StaleElementReferenceException
import datetime
from selenium.common.exceptions import NoSuchElementException


class MessagePage(JSONDate):

    def choose_the_dialog(self):
        self.click(MainPageLocators.MessageBox)
        self.click(MessagesPageLocators.UnreadMessages)

        while True:
            size = self.get_count_of_element(MessagesPageLocators.AllMessageInUnread)
            if size > 0:
                while size != 0:
                    # In this conditions: AllMessageInUndread used by once
                    time.sleep(1)
                    try:
                        self.click(MessagesPageLocators.AllMessageInUnread)
                    except NoSuchElementException:
                        self.driver.refresh()

                    size -= 1
                    print self.get_name_character("fullname")
                    foranswer = self.compare_values(MesssagesReaction.Hello)

                    if foranswer[0] is not None:
                        for element in foranswer:
                            if element == (unicode('Привет', 'utf-8')):
                                element = self.check_the_get_name(element)
                            elif element == (unicode('Часы', 'utf-8')):
                                element = self.hours_hello_answer(datetime.datetime.now().hour)
                                element = self.check_the_get_name(element)
                            for i in range(0, element.__len__()):
                                self.input_box(MessagesPageLocators.DialogBox, element[i])
                                time.sleep(0.1)

                            self.driver.find_element(*MessagesPageLocators.DialogBox).send_keys(Keys.ENTER)

                    time.sleep(1)
                    self.click(MessagesPageLocators.UnreadMessages)
                    time.sleep(1)

            else:
                pass

    def get_name_character(self, attribute):
        name = self.driver.find_element(*MessagesPageLocators.BoxWithName)
        name = name.get_attribute('text')
        if attribute == "onlyname":
            name = name[:name.find(' ')]
            return name
        else:
            return name


    @staticmethod
    def hours_hello_answer(hours):
        if 9 > hours > 3:
            return unicode('Доброе утро', 'utf-8')
        elif 15 > hours > 9:
            return unicode('Доброе день', 'utf-8')
        elif 21 > hours > 15:
            return unicode('Добрый вечер', 'utf-8')
        else:
            return unicode('Добрая ночь', 'utf-8')

    def check_the_get_name(self, element):
        try:
            name = self.get_name_character("onlyname")
            element = element + ", " + name
            return element
        except StaleElementReferenceException:
            self.driver.refresh()





