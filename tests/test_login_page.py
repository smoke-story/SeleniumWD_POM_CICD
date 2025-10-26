from config.base_test import BaseTest
import allure


@allure.feature("Login page functionality")
class TestLoginPage(BaseTest):

    allure.severity("critical")
    @allure.title("guest should see registration form")
    def test_guest_should_see_registration_form(self) -> None:
        self.login_page.open()
        self.login_page.should_be_register_form()


    @allure.severity("blocker")
    @allure.title("guest should see login form")
    def test_guest_should_see_login_form(self) -> None:
        self.login_page.open()
        self.login_page.should_be_login_form()

    
    @allure.severity("minor")
    @allure.title("guest can register")
    def test_guest_can_register(self) -> None:
        self.login_page.open()
        self.login_page.register_new_user()
        self.login_page.should_be_success_message()


    @allure.severity("normal")
    @allure.title("guest can log in")
    def test_guest_can_log_in(self) -> None:
        self.login_page.open()
        self.login_page.login_user()
        self.login_page.should_be_success_message()
