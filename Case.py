import unittest
from selenium import webdriver
from ApplicationManager import AutoPage
from MessagePages import MessagePage
import testGUI
from Tkinter import TclError


class VKTest(unittest.TestCase, AutoPage, MessagePage):

    def setUp(self):

        testGUI.main()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://vk.com/login?act=mobile&hash=5ccef1ada1b37814")

    def test_bot_start(self):
        self.login_to_vk(testGUI.my_login_data, testGUI.my_pass_data)
        self.choose_the_dialog()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
