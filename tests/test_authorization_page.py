from diplom_3.constants import Urls
from diplom_3.pages.authorization_page import AuthorizationPage
import allure


class TestAuthorizationPage:

    @allure.title("Проверить ссылку 'Забыли пароль? Восстановить пароль'")
    @allure.description('Нажать нассылку "Забыли пароль? Восстановить пароль" > проверить переход на страницу восстановления пароля')
    def test_check_click_recovery_password(self,driver_authorisation_page):
        recovery_password = AuthorizationPage(driver_authorisation_page,Urls.URL_AUTHORISATION_PAGE)
        recovery_password.click_on_link_recovery_password()
        recovery_password.check_recovery_page()

    @allure.title("Проверить заполнение поля емаил на форме Восстановить пароль")
    @allure.description('Нажать нассылку "Забыли пароль? Восстановить пароль" > проверить переход на страницу Забыли пароль > заполнить емеил '
                        '>нажать кнопку Восстановить> проверить переход на страницу восстановления пароля')
    def test_check_fill_email_and_click_recovery_password(self,driver_authorisation_page):
        recovery_password = AuthorizationPage(driver_authorisation_page,Urls.URL_AUTHORISATION_PAGE)
        recovery_password.click_on_link_recovery_password()
        recovery_password.check_recovery_page()
        recovery_password.fill_email_in_recovery_field()
        recovery_password.click_recovery_button()
        recovery_password.check_recovery_password_page()

    @allure.title("Проверить элемент 'Показать пароль'")
    @allure.description('Заполнить пароль для восстановления" > нажать на элемент Показать пароль > проверить: пароль открыт для просмотра')
    def test_check_show_hide_password(self,driver_authorisation_page):
        recovery_password = AuthorizationPage(driver_authorisation_page,Urls.URL_AUTHORISATION_PAGE)
        recovery_password.fill_recovery_password()
        recovery_password.click_button_show_hide_password()
        recovery_password.check_value_show_password()


