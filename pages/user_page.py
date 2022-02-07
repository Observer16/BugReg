from .base_page import BasePage
from .locators import UserPageLocators
import time

class UserPage(BasePage):

    def add_new_user(self, name_1, email_1, password_1, dateWithMD, noibiz_name1, surname, fathername1, adres):
        name_field = self.browser.find_element(*UserPageLocators.REGISTER_NAME)
        name_field.send_keys(name_1)
        email_field = self.browser.find_element(*UserPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email_1)
        password_field1 = self.browser.find_element(*UserPageLocators.REGISTER_PASSWORD_1)
        password_field1.send_keys(password_1)
        dateWithMD_field =  self.browser.find_element(*UserPageLocators.REGISTER_DATEWITH)
        dateWithMD_field.send_keys(dateWithMD)
        noibiz_name1_field = self.browser.find_element(*UserPageLocators.REGISTER_NAME1)
        noibiz_name1_field.send_keys(noibiz_name1)
        surname_field = self.browser.find_element(*UserPageLocators.REGISTER_SURNAME1)
        surname_field.send_keys(surname)
        fathername1_field = self.browser.find_element(*UserPageLocators.REGISTER_FATHERNAME1)
        fathername1_field.send_keys(fathername1)

        adres_field = self.browser.find_element(*UserPageLocators.REGISTER_ADRES)
        adres_field.send_keys(adres)
