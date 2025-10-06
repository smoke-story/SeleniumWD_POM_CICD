from .base_page import BasePage
from .locators import ProductPageLocators, Links
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):


    def open(self):
        self.driver.get(Links.PRODUCT_PAGE_LINK)
        self.wait.until(EC.url_contains(Links.PRODUCT_URL_PART), \
                        f"url: {Links.PRODUCT_PAGE_LINK} is not opened")


    def add_product_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()


    def should_be_product_title_in_message(self):
        product_title = self.driver.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        success_added_message = self.wait.until(
            EC.presence_of_element_located(ProductPageLocators.MESSAGE_SUCCESSFUL_ADDING)).text
        assert product_title == success_added_message, \
            f"'success added message: {success_added_message}' is not correct"


    def should_be_product_price_in_message(self):
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_message = self.wait.until(
            EC.presence_of_element_located(ProductPageLocators.MESSAGE_BASKET_PRICE)).text
        assert product_price == basket_price_message, "basket price message is not correct"


    def should_be_link_parameter_in_url(self):
        assert self.wait.until(EC.url_contains(ProductPageLocators.LINK_PARAMETER)), \
        "url is no contains offer parameter"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    

    def message_should_disappear(self):
        assert self.is_disappeared is True, \
            "Success message is presented, but should dissapeared"
    

    def click_to_add_review_button(self):
        self.driver.find_element(*ProductPageLocators.REVIEW_BUTTON).click()


    def scroll_to_review_form(self):
        self.scroll_to_element(*ProductPageLocators.REVIEW_FORM)


    def should_be_review_form(self):
        assert self.driver.find_element(*ProductPageLocators.REVIEW_FORM), \
        "there is no review form"
    
    
