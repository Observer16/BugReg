from selenium.webdriver.common.by import By

'''
Каждый класс будет соответствует каждому классу PageObject
'''

class BasePageLocators():
    CLICK_NEW_USER = (By.CSS_SELECTOR, "body > div.content > p:nth-child(2) > a")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "body > div.content > div.row > div:nth-child(1) > form")
    REGISTER_FORM = (By.CSS_SELECTOR, "body > div.content > div.row > div:nth-child(2) > form")
    REGISTER_NAME = (By.CSS_SELECTOR, "body > div.content > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "body > div.content > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "body > div.content > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input[type=password]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "body > div.content > div.row > div:nth-child(2) > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class UserPageLocators():
    REGISTER_NAME = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(1) > td.field_need.field_name > input")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(2) > td.field_need.field_email > input")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(3) > td.field_need.field_password > input")  
    REGISTER_DATEWITH = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(7) > td.field_need.field_date_start > input")
    REGISTER_ADRES = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(19) > td.field_need.field_adres > input")
    REGISTER_NAME1 = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(9) > td.field_need.field_name1 > input")
    REGISTER_SURNAME1 = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(10) > td.field_need.field_surname1 > input")
    REGISTER_FATHERNAME1 = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(11) > td.field_need.field_fathername1 > input.form-control.numberfilter")
    ADDS_BUTTON = (By.CSS_SELECTOR, "body > div.content > form > table > tbody > tr:nth-child(21) > td:nth-child(2) > input")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    