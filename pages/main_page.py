import allure
from .base_page import BasePage
from .locators import MainPageLocators, Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    @allure.step(f"open '{Links.BASE_URL}' page")
    def open(self) -> None:
        self.driver.get(Links.BASE_URL)
        self.wait.until(EC.url_contains(Links.BASE_URL),
            f"'BASE URL' is wrong. Current: {self.current_url}")


    @allure.step("should be welcome text")
    def should_be_welcome_text(self) -> None:
        assert self.is_element_present(MainPageLocators.WELCOME_TEXT), \
            "Welcome text is missing."


    @allure.step("should be promo items")
    def should_be_promo_items(self) -> None:
        assert self.is_element_present(MainPageLocators.PROMO_ITEMS), \
            "Promo items is missing."
    
