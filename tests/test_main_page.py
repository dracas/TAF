import pytest
from pytest_testrail.plugin import pytestrail
from taf.pages.main_page import MainPage
from taf.pages.login_page import LoginPage
from taf.pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytestrail.case('4')
    def test_guest_can_go_to_login_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytestrail.case('3')
    def test_guest_should_see_login_link(self, browser):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytestrail.case('5')
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_not_products_and_be_message()
