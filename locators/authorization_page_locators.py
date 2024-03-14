from selenium.webdriver.common.by import By


class AuthorizationLocators:
    NAME_FIELD = (By.XPATH, '//label[contains(text(),"Имя")]/..//input')        #поле Имя
    PERSONAL_ACCOUNT = (By.XPATH, '//a[contains(@href, "/account")]')           #кнопка "Личный кабинет"
    PASSWORD_FIELD = (By.XPATH, '//label[contains(text(),"Пароль")]/..//input')  # поле Пароль
    EMAIL_FIELD = (By.XPATH, '//label[contains(text(),"Email")]/..//input')  # поле Емаил
    LOGOUT = (By.XPATH, '//button[text()="Выход"]')                             #кнопка "Выход"
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')    #ссылка "Восстановить пароль"
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')                    #кнопка "Восстановить"
    CODE_RECOVERY_FIELD = (By.XPATH, '//label[contains(text(),"Введите код из письма")]/..//input') #поле "Введите код из письма"
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')                    #кнопка "Сохранить"
    SUBMIT_AUTHORIZATION = (By.XPATH, '//h2[contains(text(), "Вход")]')          # ссылка авторизации https://stellarburgers.nomoreparties.site/login
    BUTTON_SHOW_HIDE_PASSWORD = (By.XPATH, '//div[contains(@class,"icon-action")]')  #кнопка показать/скрыть пароль
    VALUE_SHOW_PASSWORD = (By.XPATH, '//input[@type="text"]')                    #значение показать введенный пароль
