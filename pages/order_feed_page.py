import time

from diplom_3.locators.main_page_locators import MainLocators
from diplom_3.locators.order_feed_locators import OrderFeedLocators
from diplom_3.pages.base_page import BasePage
from diplom_3.constants import ApiConstants,Constants
from diplom_3.locators.authorization_page_locators import AuthorizationLocators
import requests
import allure



class OrderFeedPage(BasePage):

    """Методы кнопок"""

    @allure.step('Нажать на заказ')
    def click_to_order(self):
        self.wait_visibility_of_element_located(OrderFeedLocators.ORDERS_LIST_LAST)
        self.click_on_element(OrderFeedLocators.ORDERS_LIST_LAST)

    @allure.step('Нажать на крестик закрыть окно заказа')
    def click_close_window_orders(self):
        self.click_on_element(OrderFeedLocators.BUTTON_CLOSE_WINDOW_ORDERS_DETAILS)

    """Методы проверки элементов страницы"""
    @allure.step("Проверить номер заказа в окне заказа")
    def check_window_order_id(self):
        assert self.wait_visibility_of_element_located(OrderFeedLocators.ORDER_NUMBER)


    @allure.step("Проверить переход на страницу 'Лента заказов'")
    def check_order_feed_page(self):
        assert self.wait_visibility_of_element_located(OrderFeedLocators.SECTION_ORDER_FEED)

    """Методы получения элементов страницы"""

    @allure.step("Получить общий счетчик заказов 'за все время'")
    def get_total_count_orders_all_time(self):
        self.wait_visibility_of_element_located(OrderFeedLocators.TOTAL_ORDERS_COUNT_ALL_TIME)
        return self.get_actually_text(OrderFeedLocators.TOTAL_ORDERS_COUNT_ALL_TIME)

    @allure.step("Получить общий счетчик заказов 'за сегодня'")
    def get_total_count_orders_today(self):
        self.wait_visibility_of_element_located(OrderFeedLocators.TOTAL_ORDERS_COUNT_TODAY)
        return self.get_actually_text(OrderFeedLocators.TOTAL_ORDERS_COUNT_TODAY)


    @allure.step('Получение номера заказа')
    def get_user_number_order(self):
        time.sleep(1)
        return self.get_actually_text(OrderFeedLocators.ORDER_NUMBER)


    @allure.step('Получение номера заказа в списке "Готовы"')
    def get_user_order_in_ready(self):
        all_elements = self.find_elements(OrderFeedLocators.LAST_ORDER_IN_LIST_READY)
        elements_text = [element.text for element in all_elements]
        return str(elements_text)


    """Метод создания новго заказа"""
    @allure.step('Создание нового заказа')
    def create_order(self):
        self.drag_and_drop_on_element(OrderFeedLocators.BUN_FLUORESCENT_ROLL_R2_D3, OrderFeedLocators.CART_BURGER_CONSTRUCTOR)
        self.drag_and_drop_on_element(OrderFeedLocators.SAUCE_SPICY_X,OrderFeedLocators.CART_BURGER_CONSTRUCTOR)
        self.drag_and_drop_on_element(OrderFeedLocators.FILLING_MEAT_OF_IMMORTAL_MOLLUSKS_PROTOSTOMIA,OrderFeedLocators.CART_BURGER_CONSTRUCTOR)
        self.click_on_element(OrderFeedLocators.BUTTON_MAKE_ORDER)

