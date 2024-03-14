from diplom_3.constants import Urls
from diplom_3.pages.base_page import BasePage
from diplom_3.locators.authorization_page_locators import AuthorizationLocators
from diplom_3.locators.main_page_locators import MainLocators
from diplom_3.locators.personal_account_page_locators import PersonalAccountLocators
from diplom_3.constants import Constants
import allure



class PersonalAccount(BasePage):

    """Методы кнопок"""

    @allure.step("Нажать на раздел История заказов")
    def click_to_history_orders(self):
        self.click_on_element(PersonalAccountLocators.HISTORY_ORDERS)
        assert self.wait_visibility_of_element_located(PersonalAccountLocators.HISTORY_ORDERS)

    @allure.step("Нажать 'Выход' в личном кабинете""")
    def click_to_button_logout(self):
        self.click_on_element(PersonalAccountLocators.LOGOUT)

    """Методы проверки элементов страницы"""
    @allure.step("Проверить переход на страницу авторизации")
    def check_authorization_page(self):
        actual_url = Urls.URL_AUTHORISATION_PAGE
        expected_url = Urls.URL_AUTHORISATION_PAGE
        assert actual_url == expected_url


    @allure.step("Проверить переход на страницу История заказов")
    def check_to_history_orders(self):
        actual_url = Urls.URL_HISTORY_ORDER
        expected_url = Urls.URL_HISTORY_ORDER
        assert actual_url == expected_url

    @allure.step("Проверить переход на страницу Личного кабинета")
    def check_to_personal_account(self):
        assert self.wait_visibility_of_element_located(PersonalAccountLocators.PROFILE)
