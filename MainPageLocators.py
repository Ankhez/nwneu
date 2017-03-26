# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    class_description = "Locators ID"

    MessageBox = (By.XPATH, "//span[text()='Сообщения']")