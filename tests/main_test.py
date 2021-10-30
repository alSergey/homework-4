from tests.helpers.default_test import DefaultTest

from pages.main import MainPage
from pages.product_card import ProductCard
from pages.search import SearchPage
from pages.product import ProductPage
from pages.login import LoginPage


class MainTest(DefaultTest):
    def setUp(self):
        super().setUp()
        self.main = MainPage(driver=self.driver)
        self.main.open()

    def testClickSearch(self):
        """Проверка, что при нажатии на кнопку "Найти" открывает страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickSearchWithParam(self):
        """Проверка, что при введенных данных в поиск и нажатии на кнопку "Найти" открывает страница поиска"""
        search = SearchPage(driver=self.driver)
        text = "test"

        self.main.input_search_value(text)
        self.main.click_search()

        url = self.driver.current_url
        search.change_path(text)
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testEnterSearch(self):
        """Проверка, что в поиске при нажатии "Enter" открывает страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.enter_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testEnterSearchWithParam(self):
        """Проверка, что при введенных данных в поиск и нажатии "Enter" открывает страница поиска"""
        search = SearchPage(driver=self.driver)
        text = "test"

        self.main.input_search_value(text)
        self.main.enter_search()

        url = self.driver.current_url
        search.change_path(text)
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickCategory(self):
        """Проверка, что при нажатии на категорию открывается страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.click_category()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product = ProductPage(driver=self.driver)
        product_card = ProductCard(driver=self.driver)

        product_id = product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Некорректный урл")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        login = LoginPage(driver=self.driver)
        product_card = ProductCard(driver=self.driver)

        product_card.like_product()
        self.assertTrue(login.is_opened(), "Не открыта авторизация")
        login.click_close()

        login.auth()

        index = product_card.like_product()
        self.assertTrue(product_card.check_like_product(index), "Не удалось поставить лайк")

        product_card.remove_like_product(index)
        self.assertFalse(product_card.check_remove_like_product(index), "Не удалось убрать лайк")
