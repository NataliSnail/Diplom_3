import time
from diplom_3.pages.order_feed_page import OrderFeedPage
from diplom_3.constants import Urls
import allure



class TestOrderFeed:

    @allure.title("Проверить заказ")
    @allure.description('Клик на хедер Лента заказов> клик на заказ> проверить открытие pop-up заказа')
    def test_check_order(self,driver):
        order = OrderFeedPage(driver,Urls.URL)
        order.click_to_order_feed_section()
        order.click_to_order()
        order.check_window_order_id()



    @allure.title("Проверить счетчик заказов за все время")
    @allure.description('Авторизоваться> проверить переход на главную страницу> клик на хедер Лента заказа> сохранить в переменную total_before текущее значение счетчика "за все время">'
                        'нажать на хедер Конструктор> создать новый заказ>убедиться что заказ сформирован> закрыть pop-up заказа> перейти в раздел Лента заказов>'
                        'сохранить в переменную total_after  новое значение счетчика "за все время"> подтвердить, что значение увеличилось ')
    def test_check_total_order_count_all_time(self,driver):
        order = OrderFeedPage(driver,Urls.URL)
        order.login_authorization()
        order.click_to_order_feed_section()
        total_before = order.get_total_count_orders_all_time()
        order.click_to_button_constructor()
        order.create_order()
        order.check_window_order_id()
        order.click_close_window_orders()
        order.click_to_order_feed_section()
        total_after = order.get_total_count_orders_all_time()
        assert total_after > total_before


    @allure.title("Проверить счетчик заказов за сегодня")
    @allure.description('Авторизоваться> проверить переход на главную страницу> клик на хедер Лента заказа> сохранить в переменную total_before текущее значение счетчика "за сегодня">'
                        'нажать на хедер Конструктор> создать новый заказ>убедиться что заказ сформирован> закрыть pop-up заказа> перейти в раздел Лента заказов>'
                        'сохранить в переменную total_after  новое значение счетчика "за сегодня"> подтвердить, что значение увеличилось ')
    def test_check_total_order_count_today(self,driver):
        order = OrderFeedPage(driver, Urls.URL)
        order.login_authorization()
        order.click_to_order_feed_section()
        total_before = order.get_total_count_orders_today()
        order.click_to_button_constructor()
        order.create_order()
        order.check_window_order_id()
        order.click_close_window_orders()
        order.click_to_order_feed_section()
        total_after = order.get_total_count_orders_today()
        assert total_after > total_before


    @allure.title("Проверить номер заказа в списке 'готово'")
    @allure.description('Авторизоваться> проверить переход на главную страницу> создать новый заказ>убедиться что заказ сформирован> закрыть pop-up заказа> перейти в раздел Лента заказов>'
                        ' проверить что номер нового заказа есть в списке заказов "Готово"')
    def test_check_order_in_ready(self, driver):
        order = OrderFeedPage(driver, Urls.URL)
        order.login_authorization()
        order.check_main_page()
        order.create_order()
        order.check_window_order_id()
        time.sleep(5)              #вынужденная мера,иначе метод берет первое значение "9999". другое предложение от наставника-чтобы тест просто падал
        new_order = order.get_user_number_order()
        order.click_close_window_orders()
        order.click_to_order_feed_section()
        order.check_order_feed_page()
        elements = order.get_user_order_in_ready()
        assert new_order in elements




