from selenium.webdriver.common.by import By


class OrderFeedLocators:

    SECTION_ORDER_FEED =(By.XPATH, '//a[contains(@href, "/feed")]')                                                     # раздел Лента заказов
    ORDERS_LIST_LAST = (By.XPATH, '//*[@class="OrderHistory_link__1iNby"][1]')                                          #последний заказ в Ленте заказов
    TOTAL_ORDERS_COUNT_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class, "digits")]')   #Выполнено за все время
    TOTAL_ORDERS_COUNT_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class, "digits")]')       #Выполнено за сегодня
    TOTAL_LIST_INGREDIENT_BURGER = (By.XPATH,'//section[@class = "BurgerConstructor_basket__29Cd7.mt-25"]')             # список добавленных ингридиентов в бургер
    COMPOUND_IN_WINDOW_INGREDIENT = (By.XPATH, '//*[@class="OrderFeed_list__OLh59"][1]')                                # "состав" в всплывающем окне ингредиентов
    WINDOW_WITH_ORDER_DETAIL = (By.CSS_SELECTOR, '[class*="Modal_modal_opened__3ISw4.Modal_modal__P3_V5"] [class= "Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X.p-10"]')  #всплывающее окно  с деталями заказа
    LAST_ORDER_IN_LIST_READY = (By.XPATH, '//li[@class="text text_type_digits-default mb-2"][1]')                       #последний заказ в списке ГОТОВЫ