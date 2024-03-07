from diplom_3.pages.personal_account_page import PersonalAccount
from diplom_3.constants import Urls
import allure




class TestPersonalAccount:

    @allure.title("Проверить Выход из личного кабинета")
    @allure.description('Клик Личный кабинет>авторизоваться> проверить переход на главную страницу> клик на хедер Личный кабинет>'
                        'клик на кнопку Выход> проверить переход на страницу авторизации')
    def test_logout(self,driver):
        account = PersonalAccount(driver, Urls.URL)
        account.click_to_personal_account()
        account.login_authorization()
        account.check_main_page()
        account.click_to_personal_account()
        account.click_to_button_logout()
        account.check_authorization_page()


    @allure.title("Проверить переход по хедеру Личный кабинет")
    @allure.description('Авторизоваться> проверить переход на главную страницу> клик на хедер Личный кабинет>'
                        'проверить переход в личный кабинет')
    def test_go_to_personal_account(self,driver):
        account = PersonalAccount(driver, Urls.URL)
        account.login_authorization()
        account.check_main_page()
        account.click_to_personal_account()
        account.check_to_personal_account()

    @allure.title("Проверить переход в раздел История заказов")
    @allure.description('Клик Личный кабинет>авторизоваться> проверить переход на главную страницу> клик на хедер Личный кабинет>'
                        'клик на История заказов> проверить переход страницы на Историю заказов')
    def test_check_click_to_history_orders(self,driver):
        account = PersonalAccount(driver, Urls.URL)
        account.click_to_personal_account()
        account.login_authorization()
        account.check_main_page()
        account.click_to_personal_account()
        account.click_to_history_orders()
        account.check_to_history_orders()