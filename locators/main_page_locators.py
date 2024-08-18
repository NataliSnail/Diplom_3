from selenium.webdriver.common.by import By


class MainLocators:
    PASSWORD_FIELD = (By.XPATH, '//label[contains(text(),"Пароль")]/..//input')  # поле Пароль
    EMAIL_FIELD = (By.XPATH, '//label[contains(text(),"Email")]/..//input')  # поле Емаил
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # кнопка "Войти"
    PERSONAL_ACCOUNT = (By.XPATH, '//a[contains(@href, "/account")]')                 #кнопка "Личный кабинет"
    CONSTRUCTOR = (By.XPATH, '//p[contains(text(), "Конструктор")]')                  #кнопка "Конструктор"
    COLLECT_TO_BURGER = (By.XPATH,'//h1[contains(text(), "Соберите бургер")]')        #"соберите бургер" на главной странице
    ORDER_FEED_SECTION = (By.XPATH,'//p[contains(text(), "Лента Заказов")]')          #хедер "лента заказов"
    ORDER_FEED_TEXT = (By.XPATH,'//h1[contains(text(), "Лента заказов")]')            #текст "Лента заказов" на странице
    ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')                        #поп-ап Идентификатор заказа
    WINDOW_ORDER = (By.XPATH,'//div[@class="Modal_modal__container__Wo2l_"]')          #поп-ап подтвержения заказа
    TEXT_YOUR_ORDER_MAKE = (By.XPATH, '//p[contains(text(), "Ваш заказ начали готовить")]')  # текст Ваш заказ начали готовить на форме id заказа
    ENERGY_VALUE_INGREDIENT = (By.XPATH, '//li[@class="Modal_modal__statsListItem__3twJZ"]') #энергетическая ценность (жиры, калории и т.д)
    COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')                     # Счетчик
    BUN_FLUORESCENT_ROLL_R2_D3 = (
    By.XPATH, '//p[contains(text(), "Флюоресцентная булка R2-D3")]')  # ингредиент Флюоресцентная булка R2-D3
    BUN_KRATOR_N_200I = (By.XPATH, '//p[contains(text(), "Краторная булка N-200i")]')  # ингредиент Краторная булка
    SAUCE_SPICY_X = (By.XPATH, '//p[contains(text(), "Соус Spicy-X")]')  # ингредиент соус "Соус Spicy-X"
    FILLING_MEAT_OF_IMMORTAL_MOLLUSKS_PROTOSTOMIA = (By.XPATH,'//p[contains(text(), "Мясо бессмертных моллюсков Protostomia")]')  # ингредиент начинка Мясо бессмертных моллюсков Protostomia
    WINDOW_INGREDIENTS_DETAILS = (By.XPATH, '//h2[contains(text(), "Детали ингредиента")]')  # поп-ап Детали ингредиента
    BUTTON_CLOSE_WINDOW_INGREDIENTS_DETAILS = (By.XPATH, '//section[contains(@class,"opened")]//button')  # крестик закрыть всплывающее окно Детали ингредиента
    CART_BURGER_CONSTRUCTOR = (By.CLASS_NAME, 'BurgerConstructor_basket__29Cd7.mt-25')  # Корзина
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')  # кнопка Оформить заказ


