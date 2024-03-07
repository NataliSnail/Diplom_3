from diplom_3.pages.main_page import MainPage
from diplom_3.constants import Urls
import allure


class TestMain:

    @allure.title("Проверить переход из Личного кабинета на хедер Конструктор")
    @allure.description('Авторизоваться> Войти в личный кабинет> кликнуть на хедер Конструктор> Проверить переход на главную страницу сайта')
    def test_check_button_constructor_from_personal_account(self,driver):
        constructor = MainPage(driver,Urls.URL)
        constructor.login_authorization()
        constructor.click_to_personal_account()
        constructor.click_to_button_constructor()
        constructor.check_main_page()


    @allure.title("Проверить переход с главной страницы сайта на хедер Лента заказов")
    @allure.description('Авторизоваться> кликнуть на хедер Лента заказов> Проверить переход на страницу заказов')
    def test_check_button_constructor_from_personal_account(self,driver):
        order_feed = MainPage(driver,Urls.URL)
        order_feed.login_authorization()
        order_feed.click_to_order_feed_section()
        order_feed.check_order_feed_page()

    @allure.title("Проверить открытие pop-up при клике на ингредиент")
    @allure.description('Клик на ингредиент> проверить открытие всплывающего окна с информацией о ингредиенте')
    def test_check_click_on_ingredients(self,driver):
        ingredient = MainPage(driver,Urls.URL)
        ingredient.click_on_ingredient()
        ingredient.check_open_window_ingredients_details()

    @allure.title("Проверить закрытие pop-up ингредиента")
    @allure.description('Клик на ингредиент> проверить открытие всплывающего окна с информацией о ингредиенте> клик на крестик "закрыть" в окне> проверить переход на главную страницу сайта')
    def test_check_close_window_on_details_ingredient(self,driver):
        ingredient = MainPage(driver,Urls.URL)
        ingredient.click_on_ingredient()
        ingredient.check_open_window_ingredients_details()
        ingredient.click_close_window_ingredients_details()
        ingredient.check_main_page()


    @allure.title("Проверить создание нового заказа")
    @allure.description('Авторизоваться в личном кабинете> проверить переход на главную страницу сайта > перетащить в корзину элемент "булка">'
                        ' перетащить в корзину элемент "соус> перетащить в корзину элемент "начинка"> клик Оформить заказ> подтвердить оформление заказа')
    def test_check_user_take_order(self,driver,):
        user = MainPage(driver,Urls.URL,)
        user.login_authorization()
        user.check_main_page()
        user.add_ingredient_bun()
        user.add_ingredient_name_sauce()
        user.add_ingredient_name_fillings()
        user.click_button_make_order()
        user.check_new_order()


