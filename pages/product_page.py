import allure
from .base_page import BasePage
from .locators import ProductPageLocators, Links
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def open(self, parameter="") -> None:
        with allure.step(f"open '{Links.PRODUCT_PAGE_LINK}{parameter}' page"):
            self.driver.get(f"{Links.PRODUCT_PAGE_LINK}{parameter}")
            assert self.wait.until(EC.url_contains(Links.PRODUCT_URL_PART)), \
                f"url: {Links.PRODUCT_PAGE_LINK} is not opened"


    @allure.step("add product to basket")
    def add_product_to_basket(self) -> None:
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()


    @allure.step("should be product title in message")
    def should_be_product_title_in_message(self) -> None:
        product_title = self.driver.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        success_added_message = self.wait.until(
            EC.presence_of_element_located(ProductPageLocators.MESSAGE_SUCCESSFUL_ADDING)).text
        assert product_title == success_added_message, \
            f"'success added message: {success_added_message}' is not correct"


    @allure.step("should be product price in message")
    def should_be_product_price_in_message(self) -> None:
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_message = self.wait.until(
            EC.presence_of_element_located(ProductPageLocators.MESSAGE_BASKET_PRICE)).text
        assert product_price == basket_price_message, \
            f"Basket price message: '{basket_price_message}' is not correct"


    @allure.step("should be link parameter in url")
    def should_be_link_parameter_in_url(self) -> None:
        assert self.wait.until(EC.url_contains(ProductPageLocators.LINK_PARAMETER)), \
            "url is no contains offer parameter"


    @allure.step("should be success message")
    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    

    @allure.step("should disappear message")
    def should_disappear_message(self) -> None:
        assert self.is_disappeared is True, \
            "Success message is presented, but should dissapeared"
    

    @allure.step("click to add review button")
    def click_to_add_review_button(self) -> None:
        self.driver.find_element(*ProductPageLocators.REVIEW_BUTTON).click()


    @allure.step("should be review form")
    def should_be_review_form(self) -> None:
        assert self.driver.find_element(*ProductPageLocators.REVIEW_FORM), \
            "there is no review form"
