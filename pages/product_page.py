from .base_page import BasePage
from .locators import ProductPageLocators, Links
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):


    def open_product_page(self, url_parameter=""):
        self.driver.get(f"{Links.PRODUCT_PAGE_LINK}{url_parameter}")
        self.wait.until(EC.url_contains(Links.PRODUCT_URL_PART), f"{Links.PRODUCT_PAGE_LINK} is not opened")


    def add_product_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    

    def message_should_dissapear(self):
        assert self.is_disappeared is True, \
            "Success message is presented, but should dissapeared"
    

    def click_to_add_review_button(self):
        self.driver.find_element(*ProductPageLocators.REVIEW_BUTTON).click()


    def scroll_to_review_form(self):
        self.scroll_to_element(*ProductPageLocators.REVIEW_FORM)


    def should_be_review_form(self):
        assert self.driver.find_element(*ProductPageLocators.REVIEW_FORM), \
        "there is no review form"
    
    
