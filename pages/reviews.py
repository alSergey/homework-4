import time
from random import randrange

from selenium.webdriver.common.by import By

from consts import TEST_USER
from helpers import Page, Component
from components import Login


class ReviewBlock(Component):
    SORT_BY_DATE = "//label[@for=\"reviews-buyer-date\"]"
    SORT_BY_RATING = "//label[@for=\"reviews-buyer-rate\"]"

    REVIEW_CARD = ".one-review"
    REVIEW_CARD_ID = "//div[@data-review-id={}]"
    PRODUCT_TITLE = "{}//a[@class=\"one-review-head-info__product\"]".format(REVIEW_CARD_ID)
    USER_TITLE = "{}//a[@class=\"one-review-head-info__user\"]".format(REVIEW_CARD_ID)

    DATE = ".one-review-head-stat__date"
    STARS = ".one-review-head-stat__rate"
    STAR_ACTIVE = ".star-active"

    def get_review_id(self):
        elements = self.helpers.get_elements(self.REVIEW_CARD)
        index = randrange(len(elements)) - 1
        return elements[index].get_attribute("data-review-id")

    def is_contains_review(self, review_id):
        return self.helpers.is_contains(self.REVIEW_CARD_ID.format(review_id), self.helpers.SELECTOR.XPATH)

    def get_product_name_url(self, review_id):
        element = self.helpers.get_element(self.PRODUCT_TITLE.format(review_id), self.helpers.SELECTOR.XPATH)
        return element.get_attribute("href")

    def click_product_name(self, review_id):
        self.helpers.click_element(self.PRODUCT_TITLE.format(review_id), self.helpers.SELECTOR.XPATH)

    def get_user_name_url(self, review_id):
        element = self.helpers.get_element(self.USER_TITLE.format(review_id), self.helpers.SELECTOR.XPATH)
        return element.get_attribute("href")

    def click_user_name(self, review_id):
        self.helpers.click_element(self.USER_TITLE.format(review_id), self.helpers.SELECTOR.XPATH)

    def set_sort_by_date(self):
        self.helpers.click_element(self.SORT_BY_DATE, self.helpers.SELECTOR.XPATH)

    def set_sort_by_ratting(self):
        self.helpers.click_element(self.SORT_BY_RATING, self.helpers.SELECTOR.XPATH)

    def check_sort_by_date(self):
        dates = self.helpers.get_elements(self.DATE)
        for i in range(len(dates) - 1):
            time1 = time.strptime(dates[i].text, "%d.%m.%Y")
            time2 = time.strptime(dates[i + 1].text, "%d.%m.%Y")
            if time1 < time2:
                return False
        return True

    def check_sort_by_rating(self):
        stars = self.helpers.get_elements(self.STARS)
        for i in range(len(stars) - 1):
            count1 = len(stars[i].find_elements(By.CSS_SELECTOR, self.STAR_ACTIVE))
            count2 = len(stars[i + 1].find_elements(By.CSS_SELECTOR, self.STAR_ACTIVE))
            if count1 < count2:
                return False
        return True


class ReviewsPage(Page):
    PATH = "/user/{}/reviews".format(TEST_USER)

    PAGE = ".reviews"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    def change_path(self, path):
        self.PATH = "/user/" + path + "/reviews"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def review_block(self):
        return ReviewBlock(self.driver)
