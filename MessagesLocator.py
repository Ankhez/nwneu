# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class MessagesPageLocators(object):
    class_description = "Locators ID"

    UnreadMessages = (By.ID, 'ui_rmenu_unread')
    BackInTheDialogs = (By.CLASS_NAME, 'im-page--back-btn _im_page_back')
    AllMessageInUnread = (By.CLASS_NAME, 'nim-dialog--name')
    BoxWithName = (By.XPATH, '//div[3]/div/span[1]/span/a')
    DialogBox = (By.XPATH, ".//*[@contenteditable='true']")
    SendButtonInDialog = (By.CLASS_NAME, 'im-send-btn im-chat-input--send _im_send im-send-btn_send')
    NumberinDialog = (By.CLASS_NAME, '_im_chat_members im-page--members')


class MesssagesReaction(object):

    class_description = "Message_XPATH"
    Hello = (By.XPATH, ".//*[@class='im-mess-stack _im_mess_stack '][last()]//li")

