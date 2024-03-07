from diplom_3.locators.main_page_locators import MainLocators
from diplom_3.locators.personal_account_page_locators import PersonalAccountLocators
from diplom_3.pages.base_page import BasePage
from diplom_3.pages.authorization_page import AuthorizationPage
from diplom_3.locators.authorization_page_locators import AuthorizationLocators
from diplom_3.locators.main_page_locators import MainLocators
from diplom_3.constants import Constants
import allure


class MainPage(BasePage):
    """Методы заполнения полей"""

    @allure.step("Авторизация пользователя")
    def login_authorization(self):
        self.click_on_element(MainLocators.PERSONAL_ACCOUNT)
        self.send_keys(AuthorizationLocators.EMAIL_FIELD, Constants.TEST_EMAIL)
        self.send_keys(AuthorizationLocators.PASSWORD_FIELD, Constants.PASSWORD)
        self.click_on_element(AuthorizationLocators.SUBMIT_BUTTON)

    """ Методы кнопок"""
    @allure.step("Нажать на кнопку 'Показать пароль'")
    def click_to_personal_account(self):
        self.click_on_element(MainLocators.PERSONAL_ACCOUNT)
        assert self.find_element(PersonalAccountLocators.PROFILE)

    @allure.step("Нажать на хедер 'Конструктор'")
    def click_to_button_constructor(self):
        self.click_on_element(MainLocators.CONSTRUCTOR)


    @allure.step("Нажать на хедер 'Лента заказав'")
    def click_to_order_feed_section(self):
        self.click_on_element(MainLocators.ORDER_FEED_SECTION)

    @allure.step("Нажать ингредиент")
    def click_on_ingredient(self):
        self.click_on_element(MainLocators.BUN_FLUORESCENT_ROLL_R2_D3)



    @allure.step("Нажать на крестик 'закрыть' pop-up")
    def click_close_window_ingredients_details(self):
        self.click_on_element(MainLocators.BUTTON_CLOSE_WINDOW_INGREDIENTS_DETAILS)


    @allure.step("Нажать на кнопку 'Оформить заказ'")
    def click_button_make_order(self):
        self.click_on_element(MainLocators.BUTTON_MAKE_ORDER)

    """ Методы перетаскивания элементов в корзину"""
    @allure.step("Переместить ингредиент в корзину (булка)")
    def add_ingredient_bun(self):
        self.drag_and_drop_on_element(MainLocators.BUN_FLUORESCENT_ROLL_R2_D3,MainLocators.CART_BURGER_CONSTRUCTOR)

    @allure.step("Переместить ингредиент в корзину (соус)")
    def add_ingredient_name_sauce(self):
        self.drag_and_drop_on_element(MainLocators.SAUCE_SPICY_X, MainLocators.CART_BURGER_CONSTRUCTOR)

    @allure.step("Переместить ингредиент в корзину (начинка)")
    def add_ingredient_name_fillings(self):
        self.drag_and_drop_on_element(MainLocators.FILLING_MEAT_OF_IMMORTAL_MOLLUSKS_PROTOSTOMIA, MainLocators.CART_BURGER_CONSTRUCTOR)

    """Метод получения значения счетчика"""

    @allure.step('Получить значение счетчика ингредиента')
    def get_count_value(self):
        return self.get_actually_text(MainLocators.COUNTER)


    """Методы проверки элементов страницы"""
    @allure.step("Подтвердить создание заказа")
    def check_new_order(self):
        self.find_element(MainLocators.ORDER_ID)
        actually_text = self.get_actually_text(MainLocators.TEXT_YOUR_ORDER_MAKE)
        expected_text = 'Ваш заказ начали готовить'
        assert actually_text == expected_text

    @allure.step("Проверить открытие pop-up ингредиента")
    def check_open_window_ingredients_details(self):
        all_elements = self.find_elements(MainLocators.ENERGY_VALUE_INGREDIENT)
        elements_text = [element.text for element in all_elements]
        assert 'Калории,ккал\n643' and 'Белки, г\n85' in elements_text

    @allure.step("Проверить переход на страницу 'Лента заказов'")
    def check_order_feed_page(self):
        assert self.wait_visibility_of_element_located(MainLocators.ORDER_FEED_TEXT)

    @allure.step("Проверить переход на главную страницу")
    def check_main_page(self):
        assert self.wait_visibility_of_element_located(MainLocators.COLLECT_TO_BURGER)








