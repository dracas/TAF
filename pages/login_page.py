from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_page_url = self.browser.current_url
        assert 'login' in current_page_url, "Substring 'login' is missing in the current URL"

    def should_be_login_form(self):
        error_text_for_login_form = "Login form is missing on 'Login or register' page"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), error_text_for_login_form

    def should_be_register_form(self):
        error_text_for_register_form = "Register form is missing on 'Login or register' page"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), error_text_for_register_form