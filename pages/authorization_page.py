from diplom_3.constants import Urls
from diplom_3.constants import Constants
from diplom_3.pages.base_page import BasePage
from diplom_3.locators.authorization_page_locators import AuthorizationLocators
from diplom_3.locators.main_page_locators import MainLocators
import allure



class AuthorizationPage(BasePage):
    """Методы заполнения полей"""

    @allure.step("Заполнить емаил для восстановления пароля")
    def fill_email_in_recovery_field(self):
        self.send_keys(AuthorizationLocators.EMAIL_FIELD,Constants.TEST_EMAIL)

    @allure.step("Заполнить пароль для восстановления пароля")
    def fill_recovery_password(self):
        self.send_keys(AuthorizationLocators.PASSWORD_FIELD,Constants.RECOVERY_PASSWORD)


    """Методы проверки элементов страницы"""

    @allure.step("Проверить страницу Забыли пароль")
    def check_recovery_page(self):
        actual_url = Urls.URL_FORGOT_PASSWORD
        expected_url = Urls.URL_FORGOT_PASSWORD
        assert actual_url == expected_url

    @allure.step("Проверить страницу Восстановления пароля")
    def check_recovery_password_page(self):
        actual_url = Urls.URL_RECOVERY_PASSWORD
        expected_url = Urls.URL_RECOVERY_PASSWORD
        assert actual_url == expected_url

    @allure.step("Проверить элемент 'показать пароль'")
    def check_value_show_password(self):
        assert self.wait_visibility_of_element_located(AuthorizationLocators.VALUE_SHOW_PASSWORD)


    """ Методы кнопок"""

    @allure.step("Нажать на кнопку 'Показать пароль'")
    def click_button_show_hide_password(self):
        self.click_on_element(AuthorizationLocators.BUTTON_SHOW_HIDE_PASSWORD)


    @allure.step("Нажать на ссылку 'Забыли пароль? Восстановить пароль'")
    def click_on_link_recovery_password(self):
        self.click_on_element(AuthorizationLocators.FORGOT_PASSWORD)


    @allure.step("Нажать на кнопку 'Восстановить пароль'")
    def click_recovery_button(self):
        self.click_on_element(AuthorizationLocators.RECOVERY_BUTTON)

