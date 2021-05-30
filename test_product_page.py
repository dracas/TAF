from .pages.product_page import ProductPage
import pytest


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