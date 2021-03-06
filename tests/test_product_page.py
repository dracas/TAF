from mimesis import Person
import pytest
from pytest_testrail.plugin import pytestrail
from taf.pages.product_page import ProductPage
from taf.pages.login_page import LoginPage
from taf.pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        person = Person('en')
        random_email = person.email(domains=['mimesis.com'])
        random_password = "gfix8S?#DT5!EJpD"
        link = "https://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(random_email, random_password)
        page.should_be_authorized_user()

    @pytestrail.case('14')
    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytestrail.case('13')
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_an_opportunity_add_product_to_basket()
        page.should_be_correct_price_and_name()


@pytest.mark.need_review
@pytestrail.case('12')
@pytest.mark.parametrize(
    'link', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
             pytest.param("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                          marks=pytest.mark.xfail),
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
             "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_an_opportunity_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_price_and_name()


@pytest.mark.xfail
@pytestrail.case('11')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_an_opportunity_add_product_to_basket()
    page.should_not_be_success_message()


@pytestrail.case('10')
def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytestrail.case('9')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_an_opportunity_add_product_to_basket()
    page.should_be_disappeared_success_message()


@pytestrail.case('8')
def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytestrail.case('6')
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytestrail.case('7')
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/google-hacking_197/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_not_products_and_be_message()