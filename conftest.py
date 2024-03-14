from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from diplom_3.constants import Urls,Constants
import pytest



@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.get(Urls.URL)
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.get(Urls.URL)

    yield browser
    browser.quit()

@pytest.fixture
def driver_authorisation_page(driver):
    driver.get(Urls.URL_AUTHORISATION_PAGE)
    yield driver
    driver.quit()



