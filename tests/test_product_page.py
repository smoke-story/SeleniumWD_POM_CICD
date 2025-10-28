import pytest
import allure
from config.base_test import BaseTest, LoginUser


@pytest.mark.user
@allure.feature("User add item to basket from product page")
class TestUserAddToBasketFromProductPage(BaseTest, LoginUser):

    @allure.severity("trivial")
    @allure.title("user can not see success message")
    def test_user_cant_see_success_message(self) -> None:
        self.product_page.open()
        self.product_page.should_not_be_success_message()

    @allure.severity("blocker")
    @allure.title("user can add product to basket")
    @pytest.mark.xfail(reason="Bug in fixing process...")
    def test_user_can_add_product_to_basket(self) -> None:
        self.product_page.open()
        self.product_page.add_product_to_basket()
        self.product_page.should_be_product_title_in_message()
        self.product_page.should_be_product_price_in_message()


@allure.feature("Product page functionality")
class TestProductPageGuest(BaseTest):

    @allure.title("guest can not see success message after adding product to basket")
    @pytest.mark.xfail(reason="Bug in fixing process...")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self) -> None:
        self.product_page.open()
        self.product_page.add_product_to_basket()
        self.product_page.should_not_be_success_message()

    @allure.severity("minor")
    @allure.title("message disappeared after adding product to basket")
    @pytest.mark.xfail(reason="Bug in fixing process...")
    def test_message_disappeared_after_adding_product_to_basket(self) -> None:
        self.product_page.open()
        self.product_page.add_product_to_basket()
        self.product_page.should_disappear_message()

    @allure.title("guest can see review form after click on write review button")
    def test_guest_can_see_review_form_after_click_on_write_review_button(self) -> None:
        self.product_page.open()
        self.product_page.click_to_add_review_button()
        self.product_page.should_be_review_form()

    @allure.severity("minor")
    @allure.title("guest should see login link on product page")
    def test_guest_should_see_login_link_on_product_page(self) -> None:
        self.product_page.open()
        self.base_page.should_be_login_link()

    @allure.severity("critical")
    @allure.title("guest can go to login page from product page")
    def test_guest_can_go_to_login_page_from_product_page(self) -> None:
        self.product_page.open()
        self.base_page.go_to_login_page()

    @allure.title("guest can not see product in basket opened from product page")
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self) -> None:
        self.product_page.open()
        self.base_page.go_to_basket_page()
        self.basket_page.should_not_be_items_in_basket()
        self.basket_page.should_be_empty_basket_message()

    @allure.severity("trivial")
    @allure.title("guest can not see success message")
    def test_guest_cant_see_success_message(self) -> None:
        self.product_page.open()
        self.product_page.should_not_be_success_message()

    @allure.severity("blocker")
    @allure.title("guest can add product to basket")
    @pytest.mark.parametrize("num",
            [_ if _ != 7 else pytest.param(7, marks=pytest.mark.xfail) for _ in range(0, 10)])
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_guest_can_add_product_to_basket(self, num) -> None:
        self.product_page.open(f"?promo=offer{num}")
        self.base_page.delete_all_cookies()
        self.product_page.should_be_link_parameter_in_url()
        self.product_page.add_product_to_basket()
        self.base_page.solve_quiz_and_get_code()
        self.product_page.should_be_product_title_in_message()
        self.product_page.should_be_product_price_in_message()
