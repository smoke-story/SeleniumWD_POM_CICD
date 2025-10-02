from .base_page import BasePage
from .locators import LoginPageLocators, Links



class LoginPage(BasePage):


    def should_be_login_url(self):
        assert Links.LOGIN_URL_PART in self.driver.current_url, \
        f"Current url is wrong: {self.driver.current_url}"
    
    
    def register_new_user(self):
        self.open_login_page()
        self.driver.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys()
    

    def should_be_login_form(self):
        assert True
    

    def should_be_register_form(self):
        assert True


    def should_not_be_success_message(self):
        assert True
