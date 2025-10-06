import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import BasePageLocators, Links
from selenium.common import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: webdriver.Chrome | webdriver.Firefox, timeout=10):

        self.driver = driver
        # self.driver.implicitly_wait(timeout)
        self.wait = WebDriverWait(self.driver, 15)
    
    
    # =============  Тестовые методы для статичных блоков сайта.  ============= #

    def should_be_user_icon(self):
        assert self.wait.until(EC.presence_of_element_located(BasePageLocators.USER_ICON)), \
        "Something wrong with user icon"


    def open_main_page(self):
        self.driver.get(Links.BASE_URL)
        self.wait.until(EC.url_contains(Links.BASE_URL),
                        f"BASE_URL is not opened. Current: {self.current_url}")


    def open_login_page(self):
        self.driver.get(Links.LOGIN_PAGE_LINK)
        self.wait.until(EC.url_contains(Links.LOGIN_URL_PART),
                        "LOGIN_PAGE_LINK is not opened")
    

    def go_to_login_page(self):
        self.driver.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.wait.until(EC.url_contains(Links.LOGIN_URL_PART),
                        "LOGIN_PAGE_LINK is not opened")

    
    def go_to_basket_page(self):
        self.driver.find_element(*BasePageLocators.BASKET_BUTTON).click()
        self.wait.until(EC.url_contains(Links.BASKET_URL_PART),
                        "BASKET_LINK is not opened")


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"


    # =====  Вспомогательные методы и свойства для объектов страниц  ===== #

    def is_element_present(self, method, selector):
        try:
            self.driver.find_element(method, selector)
        except NoSuchElementException:
            return False
        
        return True


    def is_not_element_present(self, method, selector, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=0.2).until(
                EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return True
        
        return False
    

    def is_disappeared(self, method, selector, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=0.2).until_not(
                EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return False
        
        return True


    def scroll_by_pixels(self, x_px: int=0, y_px: int=300):
        self.driver.execute_script(f"window.scrollTo({x_px}, {y_px});")
    

    def scroll_to_element(self, method, selector):
        button = self.driver.find_element(method, selector)
        button.location_once_scrolled_into_view
    

    def is_element_in_view_port(self, method, selector):
        try:
            element = self.driver.find_element(method, selector)
            is_visible = self.driver.execute_script(
                "return arguments[0].checkVisibility({checkShadows:true});", element)
            if is_visible:
                print("Элемент находится в viewport")
            else:
                print("Элемент не находится в viewport")
        except NoSuchElementException:
            print("Элемент не найден")
    

    def current_language(self):
        return self.driver.find_element(*BasePageLocators.LANGUAGE_ELEMENT).get_attribute("lang")
    
    @property
    def current_url(self):
        return self.driver.current_url


    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        print("ОТВЕТ:", answer)
        alert.send_keys(answer)
        alert.accept()
        # try:
        #     alert = self.driver.switch_to.alert
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")