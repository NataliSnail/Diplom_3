from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    CHECKOUT = (By.XPATH, '//button[text()="Оформить заказ"]')                  #кнопка "Оформить заказ"
    PERSONAL_ACCOUNT = (By.XPATH, '//a[contains(@href, "/account")]')           #кнопка "Личный кабинет"
    LOGOUT = (By.XPATH, '//button[text()="Выход"]')                             #кнопка "Выход"
    PROFILE = (By.XPATH, '//a[contains(@href, "/account/profile")]')            #ссылка "Профиль" в Личном кабинете
    HISTORY_ORDERS = (By.XPATH, '//a[contains(@href, "/account/order-history")]')  # раздел История заказов в Личном кабинете
