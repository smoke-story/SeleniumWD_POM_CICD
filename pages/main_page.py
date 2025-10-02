from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_welcome_text(self):
        assert self.is_element_present(*MainPageLocators.WELCOME_TEXT), \
            "Welcome text is missing."
    

    def should_be_promo_items(self):
        assert self.is_element_present(*MainPageLocators.PROMO_ITEMS), \
            "Promo items is missing."
    
