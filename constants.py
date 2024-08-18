from faker import Faker

class Constants:
    faker = Faker()

    TEST_EMAIL = 'cat133@mail.ru'
    PASSWORD = '123456'
    RECOVERY_PASSWORD = 'dsfsdfsfv'
    CODE_RECOVERY_PASSWORD = "1234567"
    INCORRECT_PASSWORD = '1234'
    NAME_FIELD = "Ivan"
    PAYLOAD = {
        "email": faker.email(),
        "password": faker.random_int(100000, 999999),
        "name": faker.name()
    }


class Urls:
    URL = 'https://stellarburgers.nomoreparties.site/'
    URL_AUTHORISATION_PAGE = 'https://stellarburgers.nomoreparties.site/login'
    URL_REGISTRATION_PAGE = 'https://stellarburgers.nomoreparties.site/register'
    URL_ORDER_FEED = 'https://stellarburgers.nomoreparties.site/feed'
    URL_FORGOT_PASSWORD = 'https://stellarburgers.nomoreparties.site/forgot-password'
    URL_RECOVERY_PASSWORD = 'https://stellarburgers.nomoreparties.site/reset-password'
    URL_HISTORY_ORDER = 'https://stellarburgers.nomoreparties.site/account/order-history'
    CREATE_LOGIN_URL = 'https://stellarburgers.nomoreparties.site/api/auth/register'

class ApiConstants:
    CREATE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    DELETE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    ORDER = 'https://stellarburgers.nomoreparties.site/api/orders'
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}