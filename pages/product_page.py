from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_an_opportunity_add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_correct_price_and_name(self):
        self.should_be_the_same_price()
        self.should_be_the_same_name()

    def should_be_the_same_price(self):
        price_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE).text
        real_price = self.browser.find_element(*ProductPageLocators.THE_PRICE_OF_THE_PRODUCT).text
        assert price_in_message == real_price, "Incorrect price is displayed after the product added"

    def should_be_the_same_name(self):
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        real_name = self.browser.find_element(*ProductPageLocators.THE_PRODUCT_NAME).text
        assert name_in_message == real_name, "Incorrect name is displayed after the product added"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message was not disappeared, but should was"