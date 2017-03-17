from BasicActions import BasicAction
from page_authorization_locators import APageLocators, LoginInfo


Logininfo = LoginInfo("kurachiek@mail.ru", "120461rofl")


class AutoPage(BasicAction):

    def login_to_vk(self, name, password):
        self.input_box(APageLocators.mail_input, name)
        self.input_box(APageLocators.pass_input, password)
        self.click(APageLocators.login_button)
1






