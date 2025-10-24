import pytest
import allure
from config.base_test import BaseTest, LoginUser


@pytest.mark.login_guest
@allure.feature("Guest can login from main page")
class TestLoginFromMainPage(BaseTest):

    @allure.title("guest should see login link")
    def test_guest_should_see_login_link(self) -> None:
        self.main_page.open()
        self.base_page.should_be_login_link()


    @allure.title("guest can go to login page")
    def test_guest_can_go_to_login_page(self) -> None:
        self.main_page.open()
        self.base_page.should_be_login_link()
        self.base_page.go_to_login_page()
        self.login_page.should_be_login_url()


@allure.feature("Functionality with authorized user")
class TestMainPageUserAuthorized(BaseTest, LoginUser):

    @allure.title("user can see welcome text")
    @pytest.mark.xfail(reason="bug in fixing process...")
    def test_user_can_see_welcome_text(self) -> None:
        self.main_page.open()
        self.main_page.should_be_welcome_text()


    @allure.title("user can see promo items")
    @pytest.mark.xfail(reason="bug in fixing process...")
    def test_user_can_see_promo_items(self) -> None:
        self.main_page.open()
        self.main_page.should_be_promo_items()


@allure.feature("Main page functionality")
class TestMainPageGuest(BaseTest):

    @allure.title("guest cant see product in basket opened from main page")
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self) -> None:
        self.main_page.open()
        self.base_page.go_to_basket_page()
        self.basket_page.should_not_be_items_in_basket()
        self.basket_page.should_be_empty_basket_message()
    