
import time
from diplom_3.pages.order_feed_page import OrderFeedPage
from diplom_3.pages.main_page import MainPage
from diplom_3.constants import Urls
import allure



class TestOrderFeed:

    @allure.title("Проверить заказ")
    @allure.description('Клик на хедер Лента заказов> клик на заказ> проверить открытие pop-up заказа')
    def test_check_order(self,driver):
        order_main = MainPage(driver, Urls.URL)
        order_main.click_to_order_feed_section()

        order = OrderFeedPage(driver,Urls.URL)
        order.click_to_order()
        order.check_window_order_id()



    @allure.title("Проверить счетчик заказов за все время")
    @allure.description('Авторизоваться> проверить переход на главную страницу > клик на хедер Лента заказа> сохранить в переменную total_before текущее значение счетчика "за все время">'
                        'нажать на хедер Конструктор> создать новый заказ>убедиться что заказ сформирован> закрыть pop-up заказа> перейти в раздел Лента заказов>'
                        'сохранить в переменную total_after  новое значение счетчика "за все время"> подтвердить, что значение увеличилось ')
    def test_check_total_order_count_all_time(self,driver):
        order_main = MainPage(driver,Urls.URL)
        order_main.login_authorization()
        order_main.check_main_page()
        order_main.click_to_order_feed_section()

        order = OrderFeedPage(driver,Urls.URL)
        total_before = order.get_total_count_orders_all_time()

        order_main.click_to_button_constructor()

        order.create_order()
        order.check_window_order_id()
        order.click_close_window_orders()

        order_main.click_to_order_feed_section()

        total_after = order.get_total_count_orders_all_time()
        assert total_after > total_before


    @allure.title("Проверить счетчик заказов за сегодня")
    @allure.description('Авторизоваться> проверить переход на главную страницу > клик на хедер Лента заказа> сохранить в переменную total_before текущее значение счетчика "за сегодня">'
                        'нажать на хедер Конструктор> создать новый заказ>убедиться что заказ сформирован> закрыть pop-up заказа> перейти в раздел Лента заказов>'
                        'сохранить в переменную total_after  новое значение счетчика "за сегодня"> подтвердить, что значение увеличилось ')
    def test_check_total_order_count_today(self,driver):
        order_main = MainPage(driver, Urls.URL)
        order_main.login_authorization()
        order_main.check_main_page()
        order_main.click_to_order_feed_section()

        order = OrderFeedPage(driver, Urls.URL)
        total_before = order.get_total_count_orders_today()

        order_main.click_to_button_constructor()

        order.create_order()
        order.check_window_order_id()
        order.click_close_window_orders()

        order_main.click_to_order_feed_section()

        total_after = order.get_total_count_orders_today()
        assert total_after > total_before


    @allure.title("Проверить номер заказа в списке 'готово'")
    @allure.description('Авторизоваться> проверить переход на главную страницу> создать новый заказ>убедиться что заказ сформирован> закрыть pop-up заказа> перейти в раздел Лента заказов>'
                        ' проверить что номер нового заказа есть в списке заказов "Готово"')
    def test_check_order_in_ready(self, driver):
        order_main = MainPage(driver, Urls.URL)
        order_main.login_authorization()
        order_main.check_main_page()

        order = OrderFeedPage(driver, Urls.URL)
        order.create_order()
        order.check_window_order_id()
        new_order = order.get_user_number_order()
        order.click_close_window_orders()

        order_main.click_to_order_feed_section()

        order.check_order_feed_page()
        elements = order.get_user_order_in_ready()
        assert new_order in elements



