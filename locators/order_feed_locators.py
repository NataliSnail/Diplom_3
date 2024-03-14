from selenium.webdriver.common.by import By


class OrderFeedLocators:

    SECTION_ORDER_FEED =(By.XPATH, '//a[contains(@href, "/feed")]')                                                     #раздел Лента заказов
    ORDERS_LIST_LAST = (By.XPATH, '//*[@class="OrderHistory_link__1iNby"][1]')                                          #последний заказ в Ленте заказов
    TOTAL_ORDERS_COUNT_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class, "digits")]')  #Выполнено за все время
    TOTAL_ORDERS_COUNT_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class, "digits")]')       #Выполнено за сегодня
    TOTAL_LIST_INGREDIENT_BURGER = (By.XPATH,'//section[@class = "BurgerConstructor_basket__29Cd7.mt-25"]')             #список добавленных ингридиентов в бургер
    COMPOUND_IN_WINDOW_INGREDIENT = (By.XPATH, '//*[@class="OrderFeed_list__OLh59"][1]')                                #"состав" в всплывающем окне ингредиентов
    WINDOW_WITH_ORDER_DETAIL = (By.CSS_SELECTOR, '[class*="Modal_modal_opened__3ISw4.Modal_modal__P3_V5"] [class= "Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X.p-10"]')  #всплывающее окно  с деталями заказа
    LAST_ORDER_IN_LIST_READY = (By.XPATH, '//li[@class="text text_type_digits-default mb-2"][1]')                       #последний заказ в списке ГОТОВЫ
    ORDER_NUMBER =(By.XPATH, '//*[contains(@class, "type_digits-large")]')                                              #номер заказа
    BUTTON_CLOSE_WINDOW_ORDERS_DETAILS = (By.XPATH, '//section[contains(@class,"opened")]//button')                     #крестик закрыть всплывающее окно заказа
    DEFAULT_ORDER_NUMBER = By.XPATH, '//h2[text()="9999"]'                                                              #дефолтный номер заказа='9999'
    BUN_FLUORESCENT_ROLL_R2_D3 = (By.XPATH, '//p[contains(text(), "Флюоресцентная булка R2-D3")]')                      #ингредиент Флюоресцентная булка R2-D3
    BUN_KRATOR_N_200I = (By.XPATH, '//p[contains(text(), "Краторная булка N-200i")]')                                   #ингредиент Краторная булка
    SAUCE_SPICY_X = (By.XPATH, '//p[contains(text(), "Соус Spicy-X")]')                                                 #ингредиент соус "Соус Spicy-X"
    FILLING_MEAT_OF_IMMORTAL_MOLLUSKS_PROTOSTOMIA = (By.XPATH,'//p[contains(text(), "Мясо бессмертных моллюсков Protostomia")]')  #ингредиент начинка Мясо бессмертных моллюсков Protostomia
    WINDOW_INGREDIENTS_DETAILS = (By.XPATH, '//h2[contains(text(), "Детали ингредиента")]')                             #поп-ап Детали ингредиента
    BUTTON_CLOSE_WINDOW_INGREDIENTS_DETAILS = (By.XPATH, '//section[contains(@class,"opened")]//button')                #крестик закрыть всплывающее окно Детали ингредиента
    CART_BURGER_CONSTRUCTOR = (By.CLASS_NAME, 'BurgerConstructor_basket__29Cd7.mt-25')                                  #Корзина
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')                                      #кнопка Оформить заказ
