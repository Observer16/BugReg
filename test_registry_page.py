import datetime
from .pages.login_page import LoginPage
from .pages.user_page import UserPage
import pytest
import faker
import os

@pytest.mark.user
def test_setup(browser):
    link = "http://users.bugred.ru/user/login/"
    page = LoginPage(browser, link)
    page.open()
    f = faker.Faker()
    name = f.name()
    email = f.email()
    password = f.password()
    print(name)
    print(email)
    print(password)
    page.register_new_user(name, email, password)

# Добавляем новых пользователей
    for x in range(200):
        page.click_new_user()
        page_user = UserPage(browser, link)
        f = faker.Faker()
        name_1 = f.name()
        email_1 = f.email()
        password_1 = f.password()
# Добавить текущую дату
        now = datetime.datetime.now()
        day = now.strftime("%d")
        modeDay = int(day) - int(1)
        dateWithMD = now.strftime(str(modeDay) + "." + "%m.%Y")

# Добовить адресс
        adres = f.address()

# Загрузка Аватор
        current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
        file_path = os.path.join(current_dir, 'file-6cd27ff4e2c7619522737d6a3e30e1cd.jpeg')           # добавляем к этому пути имя файла
        uplo = browser.find_element_by_tag_name('input[type="file"]')
        uplo.send_keys(file_path)

        noibiz_name1 = ("Свободу")
        surname = ("Алексею")
        fathername1 = ("Навальному")
        page_user.add_new_user(name_1, email_1, password_1, dateWithMD, noibiz_name1, surname, fathername1, adres)