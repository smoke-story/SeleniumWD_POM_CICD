from .base_page import BasePage
from .locators import MainPageLocators, Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def open(self):
        self.driver.get(Links.BASE_URL)
        self.wait.until(EC.url_contains(Links.BASE_URL), f"url: {Links.BASE_URL} is not opened")


    def should_be_welcome_text(self):
        assert self.is_element_present(*MainPageLocators.WELCOME_TEXT), \
            "Welcome text is missing."
    

    def should_be_promo_items(self):
        assert self.is_element_present(*MainPageLocators.PROMO_ITEMS), \
            "Promo items is missing."
    
