import pytest
from ..config.base_test import BaseTest as page


@pytest.mark.login_guest
class TestLoginFromMainPage(page):

    def test_guest_can_go_to_login_page(self) -> None:
        self.base_page.open_main_page()
        self.base_page.should_be_login_link()
        self.base_page.go_to_login_page()
        self.login_page.should_be_login_url()


    def test_guest_should_see_login_link(self) -> None:
        self.base_page.open_main_page()
        self.base_page.should_be_login_link()
          


class TestUserAuthorized(page):

    def test_user_can_see_welcome_text(self) -> None:
        self.base_page.open_main_page()
        self.main_page.should_be_welcome_text()


    def test_user_can_see_promo_items(self) -> None:
        self.base_page.open_main_page()
        self.main_page.should_be_promo_items()



def test_guest_cant_see_product_in_basket_opened_from_main_page() -> None:
    page.base_page.open_main_page()
    page.base_page.go_to_basket_page()
    page.basket_page.should_not_be_items_in_basket()
    page.basket_page.should_be_empty_basket_message()
    