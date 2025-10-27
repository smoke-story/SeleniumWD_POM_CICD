import math
import allure
from selenium import webdriver
from .locators import BasePageLocators, Links
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: webdriver.Chrome | webdriver.Firefox) -> None:
        self.driver = driver
        # self.driver.implicitly_wait(timeout)
        self.wait = WebDriverWait(self.driver, timeout=15, poll_frequency=1)

    # =============  Тестовые методы для статичных блоков сайта.  =============

    @allure.step(f"Go to login page: '{BasePageLocators.LOGIN_LINK}'")
    def go_to_login_page(self) -> None:
        self.driver.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.wait.until(EC.url_contains(Links.LOGIN_URL_PART),
                        "LOGIN_PAGE_LINK is not opened")

    @allure.step(f"Go to basket page: '{BasePageLocators.BASKET_BUTTON}'")
    def go_to_basket_page(self) -> None:
        self.driver.find_element(*BasePageLocators.BASKET_BUTTON).click()
        self.wait.until(EC.url_contains(Links.BASKET_URL_PART),
                        "BASKET_LINK is not opened")

    @allure.step("Should be login link")
    def should_be_login_link(self) -> None:
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), \
                        "Login link is not presented"

    @allure.step("Should be user icon")
    def should_be_user_icon(self) -> None:
        self.wait.until(EC.presence_of_element_located(BasePageLocators.USER_ICON),
                        "Something wrong with user icon")

    # =====  Вспомогательные методы и свойства для объектов страниц  ===== #

    def is_element_present(self, locator) -> bool:
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, locator, timeout=4) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False

    def is_appeared(self, locator, timeout=4) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True

    def is_disappeared(self, locator, timeout=4) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True

    def scroll_by_pixels(self, x_pixels: int = 0, y_pixels: int = 300) -> None:
        self.driver.execute_script(f"window.scrollTo({x_pixels}, {y_pixels});")

    def scroll_to_element(self, locator) -> None:
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", element)

    def is_element_in_view_port(self, locator) -> None:
        try:
            element = self.driver.find_element(*locator)
            is_visible = self.driver.execute_script(
                "return arguments[0].checkVisibility({checkShadows:true});", element)
            if is_visible:
                print("Элемент находится в viewport")
            else:
                print("Элемент не находится в viewport")
        except NoSuchElementException:
            print("Элемент не найден")

    @property
    def current_language(self) -> str | None:
        language = self.driver.find_element(*BasePageLocators.LANGUAGE_ELEMENT)
        return language.get_attribute("lang")

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def show_cookies_in_console(self) -> None:
        print("All current cookies: ")
        [print(i, end="\n") for i in self.driver.get_cookies()]

    def delete_all_cookies(self) -> None:
        print("cleaning cookies.....")
        self.driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
        self.driver.refresh()

    def solve_quiz_and_get_code(self) -> None:
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        print("Answer:", answer)
        alert.send_keys(answer)
        alert.accept()
