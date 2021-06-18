from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_not_products_and_be_message(self):
        self.should_be_not_products()
        self.should_be_text_about_products_absent()

    def should_be_not_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_ARE_IN_BASKET), \
            "Products are present in the basket"

    def should_be_text_about_products_absent(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_PRODUCTS_ABSENT).text
        correct_message = "Your basket is empty. Continue shopping"
        assert message == correct_message, "Message 'products absent' is different or absent"