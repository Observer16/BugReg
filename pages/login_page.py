from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):          # Реализуется проверка, что подстрока "login" есть в текущем url браузера
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):         # Проверяется наличие формы
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        

    def should_be_register_form(self):         # Проверяется наличие формы
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, name, email, password):
        name_field = self.browser.find_element(*LoginPageLocators.REGISTER_NAME)
        name_field.send_keys(name)
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_field1.send_keys(password)
        button_submit =  self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_submit.click()