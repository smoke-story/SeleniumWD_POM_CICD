import pytest
from config.base_test import BaseTest, LoginUser


class TestUserAddToBasketFromProductPage(BaseTest, LoginUser):

    def test_user_cant_see_success_message(self) -> None:
        self.product_page.open()
        self.product_page.should_not_be_success_message()


    def test_user_can_add_product_to_basket (self) -> None:
        self.product_page.open()
        self.product_page.add_product_to_basket()


# class TestGuest(BaseTest):
#
#     @pytest.mark.xfail(reason="Bug in fixing process...")
#     def test_guest_cant_see_success_message_after_adding_product_to_basket(self) -> None:
#         self.product_page.open_product_page()
#         self.product_page.add_product_to_basket()
#         self.product_page.should_not_be_success_message()
#
#
#     @pytest.mark.xfail(reason="Bug in fixing process...")
#     def test_message_disappeared_after_adding_product_to_basket(self) -> None:
#         self.product_page.open_product_page()
#         self.product_page.add_product_to_basket()
#         self.product_page.message_should_disappear()
#
#
#     def test_guest_can_see_review_form_after_click_on_write_review_button(self) -> None:
#         self.product_page.open_product_page()
#         self.product_page.click_to_add_review_button()
#         self.product_page.should_be_review_form()
#
#
#     def test_guest_should_see_login_link_on_product_page(self) -> None:
#         self.product_page.open_product_page()
#         self.base_page.should_be_login_link()
#
#
#     def test_guest_can_go_to_login_page_from_product_page(self) -> None:
#         self.product_page.open_product_page()
#         self.base_page.go_to_login_page()
#
#
#     def test_guest_cant_see_product_in_basket_opened_from_product_page(self) -> None:
#         self.product_page.open_product_page()
#         self.base_page.go_to_basket_page()
#         self.basket_page.should_not_be_items_in_basket()
#         self.basket_page.should_be_empty_basket_message()
#
#
#     def test_guest_cant_see_success_message(self) -> None:
#         self.product_page.open_product_page()
#         self.product_page.should_not_be_success_message()
#
#
#     @pytest.mark.parametrize("num", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#     def test_guest_can_add_product_to_basket (self, num) -> None:
#         self.product_page.open_product_page(f"?promo=offer{num}")
#         self.product_page.should_be_link_parameter_in_url()
#         self.product_page.add_product_to_basket()
#         self.base_page.solve_quiz_and_get_code()
#         self.product_page.should_be_product_title_in_message()
#         self.product_page.should_be_product_price_in_message()
