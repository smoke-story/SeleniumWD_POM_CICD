import pytest
from ..config.base_test import BaseTest as page



# class TestUserAddToBasketFromProductPage(page):


#     def test_user_cant_see_success_message(self) -> None:
#         page.product_page.open_product_page()
#         page.product_page.should_not_be_success_message()


#     def test_user_can_add_product_to_basket (self) -> None:
#         page.product_page.open_product_page()
#         page.product_page.add_product_to_basket()



# @pytest.mark.xfail(reason="Bug in fixing process...")
# def test_guest_cant_see_success_message_after_adding_product_to_basket() -> None:
#     page.product_page.open_product_page()
#     page.product_page.add_product_to_basket()
#     page.product_page.should_not_be_success_message()


# @pytest.mark.xfail(reason="Bug in fixing process...")
# def test_message_disappeared_after_adding_product_to_basket() -> None:
#     page.product_page.open_product_page()
#     page.product_page.add_product_to_basket()
#     page.product_page.message_should_dissapear()


# def test_guest_can_see_review_form_after_click_on_write_review_button() -> None:
#     page.product_page.open_product_page()
#     page.product_page.click_to_add_review_button()
#     page.product_page.should_be_review_form()


# def test_guest_should_see_login_link_on_product_page() -> None:
#     page.product_page.open_product_page()
#     page.base_page.should_be_login_link()


# def test_guest_can_go_to_login_page_from_product_page() -> None:
#     page.product_page.open_product_page()
#     page.base_page.go_to_login_page()


# def test_guest_cant_see_product_in_basket_opened_from_product_page() -> None:
#     page.product_page.open_product_page()
#     page.base_page.go_to_basket_page()
#     page.basket_page.should_not_be_items_in_basket()
#     page.basket_page.should_be_empty_basket_message()


# def test_guest_cant_see_success_message(self) -> None:
#     page.product_page.open_product_page()
#     page.product_page.should_not_be_success_message()


@pytest.mark.parametrize("parameter, num", [["?promo=offer"],
                                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
def test_guest_can_add_product_to_basket (parameter, num) -> None:
    page.product_page.open_product_page((parameter+num))
    page.product_page.add_product_to_basket()
