import unittest
from selenium import webdriver

from pages import MainPage, RegistrationPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.main = MainPage(driver=self.driver)
        self.main.open()

    def testCloseAuth(self):
        """Проверка, что при попап открывается и закрывается"""
        self.main.login.open_auth()
        self.assertTrue(self.main.login.is_opened(), "Закрыта авторизация")
        self.main.login.click_close()
        self.assertFalse(self.main.login.is_opened(), "Открыта авторизация")

        # TODO: не работает click_outside (он не закрывает попап)
        # self.main.login.open_auth()
        # self.assertTrue(self.main.login.is_opened(), "Закрыта авторизация")
        # self.main.login.click_outside()
        # self.assertFalse(self.main.login.is_opened(), "Открыта авторизация")

    # def __test_telephone__(self, test):
    #     self.main.login.clear_telephone_value()
    #     self.main.login.input_telephone_value(test)
    #     self.main.login.enter_submit()
    #     # TODO: не понятно как проверять ошибку. У нас стандартная браузерная
    #     self.assertFalse(self.main.login.is_logined(), "Залогинен")
    #
    # def testErrorTelephoneInput(self):
    #     # авторизация с пустым телефоном
    #     test1 = ""
    #     # авторизация с телефоном, где меньше 10
    #     test2 = "111111111"
    #
    #     self.main.login.open_auth()
    #
    #     self.__test_telephone__(test1)
    #     self.__test_telephone__(test2)
    #
    # def __test_password__(self, test):
    #     self.main.login.clear_password_value()
    #     self.main.login.input_password_value(test)
    #     self.main.login.enter_submit()
    #     # TODO: не понятно как проверять ошибку. У нас стандартная браузерная
    #     self.assertFalse(self.main.login.is_logined(), "Залогинен")
    #
    # def testErrorPasswordInput(self):
    #     # авторизация с пустым паролем
    #     test1 = ""
    #     # авторизация с телефоном, где меньше 10
    #     test2 = "Qwerty12"
    #
    #     self.main.login.open_auth()
    #
    #     self.__test_password__(test1)
    #     self.__test_password__(test2)

    def testClickRegistration(self):
        """Проверка, что при нажатии кнопки "Создайте аккаунт" открывается страница регистрации"""
        registration = RegistrationPage(driver=self.driver)

        self.main.login.open_auth()
        self.main.login.click_registration()

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Некорректный урл")

    def __test_login__(self, telephone, password):
        self.main.login.clear_telephone_value()
        self.main.login.input_telephone_value(telephone)
        self.main.login.clear_password_value()
        self.main.login.input_password_value(password)

        self.login.enter_submit()
        self.assertTrue(self.main.login.is_error(), "Залогинен")

    def testErrorLogin(self):
        """Проверка ошибочной авторизации"""
        # TODO: поменять когда добавим login в ENV

        # авторизация с неправильным телефоном
        telephone1 = "0000000000"
        password1 = "Qwerty123"

        # авторизация с неправильным паролем
        telephone2 = "4444444444"
        password2 = "Qwerty12"

        self.main.login.open_auth()

        self.__test_login__(telephone1, password1)
        self.__test_login__(telephone2, password2)

    def testSuccessLogin(self):
        """Проверка успешной авторизации"""
        # TODO: поменять когда добавим login в ENV
        telephone = "4444444444"
        password = "Qwerty123"

        self.main.login.open_auth()
        self.main.login.input_telephone_value(telephone)
        self.main.login.input_password_value(password)

        self.main.login.enter_submit()
        self.assertTrue(self.main.login.is_logined(), "Не залогинен")

    def tearDown(self):
        self.driver.close()
