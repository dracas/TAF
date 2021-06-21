from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group :first-child.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form button")


class BasketPageLocators:
    PRODUCTS_ARE_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_ABOUT_PRODUCTS_ABSENT = (By.CSS_SELECTOR, "#content_inner p")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    THE_PRICE_OF_THE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    THE_PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")