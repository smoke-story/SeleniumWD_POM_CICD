import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import LoginPageLocators
from .data import Data


class BaseTest:

    data: Data
    base_page: BasePage
    basket_page: BasketPage
    login_page: LoginPage
    main_page: MainPage
    product_page: ProductPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver: webdriver.Chrome | webdriver.Firefox) -> None:
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.base_page = BasePage(driver)
        request.cls.basket_page = BasketPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.product_page = ProductPage(driver)


class LoginUser:
    
    @allure.title("Preparing to user login...")
    @pytest.fixture(autouse=True)
    def login_setup(self, driver: webdriver.Chrome | webdriver.Firefox) -> None:
        base_page = BasePage(driver)
        driver.get("https://selenium1py.pythonanywhere.com/ru/accounts/login/")
        base_page.wait.until(EC.url_contains("accounts/login"), \
                             f"url is not correct: {driver.current_url}")
        base_page.delete_all_cookies()
        driver.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        base_page.should_be_user_icon()
