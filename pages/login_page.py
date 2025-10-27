import random
import allure
from .base_page import BasePage
from .locators import LoginPageLocators, Links
from config.data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    @allure.step(f"open: '{Links.LOGIN_PAGE_LINK}'")
    def open(self) -> None:
        self.driver.get(Links.LOGIN_PAGE_LINK)
        self.wait.until(EC.url_contains(Links.LOGIN_URL_PART),
            f"login url is not correct: '{self.current_url}'")

    @allure.step("should be login url")
    def should_be_login_url(self) -> None:
        WebDriverWait(self.driver, 4).until(EC.url_contains(Links.LOGIN_URL_PART),
            f"login url is not correct: '{self.current_url}'")

    @allure.step("should be login form")
    def should_be_login_form(self) -> None:
        assert self.driver.find_element(*LoginPageLocators.REGISTER_FORM), \
            "Registering form is not present"

    @allure.step("should be register form")
    def should_be_register_form(self) -> None:
        assert self.driver.find_element(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not present"

    @allure.step("should be success message")
    def should_be_success_message(self) -> None:
        assert self.is_appeared(LoginPageLocators.SUCCESS_MESSAGE), \
            "'success message' is not present"

    @allure.step("should not be success message")
    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(LoginPageLocators.SUCCESS_MESSAGE), \
            "'success message' is present"

    @allure.step("log in user")
    def login_user(self) -> None:
        self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(Data.LOGIN)
        self.driver.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(Data.PASSWORD)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("register new user")
    def register_new_user(self) -> None:
        random_mail = f"mail{random.randint(12345, 99878)}@gg.hyz"
        random_password = f"ABcd{random.randint(1232132, 9878953)}"
        self.driver.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(random_mail)
        self.driver.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(random_password)
        self.driver.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(random_password)
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
