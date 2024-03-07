from diplom_3.constants import Urls
from diplom_3.pages.base_page import BasePage
from diplom_3.locators.authorization_page_locators import AuthorizationLocators
from diplom_3.locators.main_page_locators import MainLocators
from diplom_3.locators.personal_account_page_locators import PersonalAccountLocators
from diplom_3.constants import Constants
import allure



class PersonalAccount(BasePage):
    """Методы заполнения полей"""

    @allure.step("Авторизация пользователя")
    def login_authorization(self):
        self.click_on_element(MainLocators.PERSONAL_ACCOUNT)
        self.send_keys(AuthorizationLocators.EMAIL_FIELD, Constants.TEST_EMAIL)
        self.send_keys(AuthorizationLocators.PASSWORD_FIELD, Constants.PASSWORD)
        self.click_on_element(AuthorizationLocators.SUBMIT_BUTTON)


    """Методы кнопок"""
    @allure.step("Нажать на хедер Личный кабинет")
    def click_to_personal_account(self):
        self.click_on_element(MainLocators.PERSONAL_ACCOUNT)


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
        expected_url = 'https://stellarburgers.nomoreparties.site/login'
        assert actual_url == expected_url

    @allure.step("Проверить переход на главную страницу")
    def check_main_page(self):
        assert self.wait_visibility_of_element_located(MainLocators.COLLECT_TO_BURGER)

    @allure.step("Проверить переход на страницу История заказов")
    def check_to_history_orders(self):
        actual_url = Urls.URL_HISTORY_ORDER
        expected_url = 'https://stellarburgers.nomoreparties.site/account/order-history'
        assert actual_url == expected_url

    @allure.step("Проверить переход на страницу Личного кабинета")
    def check_to_personal_account(self):
        assert self.wait_visibility_of_element_located(PersonalAccountLocators.PROFILE)