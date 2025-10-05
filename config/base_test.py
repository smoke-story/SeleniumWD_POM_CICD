import pytest
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

class BaseTest:

    base_page: BasePage
    basket_page: BasketPage
    login_page: LoginPage
    main_page: MainPage
    product_page: ProductPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):

        request.cls.driver = driver
        request.cls.base_page = BasePage(driver)
        request.cls.basket_page = BasketPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.product_page = ProductPage(driver)

    