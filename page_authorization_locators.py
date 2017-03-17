from selenium.webdriver.common.by import By


class APageLocators(object):
    class_description = "Locators ID"

    mail_input = (By.ID, 'quick_email')
    pass_input = (By.ID, 'quick_pass')
    login_button = (By.ID, 'quick_login_button')


class LoginInfo(object):
    class_description = "Login Info"

    def __init__(self, login, password):
        self.login = login
        self.password = password
