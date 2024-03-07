from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open_to_site(self):
         self.driver.get(self.url)


    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')


    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Elements not found in {locator}')


    def wait_visibility_of_element_located(self, locator, time=50):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f'Element not found in {locator}')


    def click_on_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}').click()


    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)


    def scroll_down_page(self, locator, time=10):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url


    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text


    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


    def drag_and_drop_on_element(self, locator_element, locator_cart):
        element = self.driver.find_element(*locator_element)
        cart = self.driver.find_element(*locator_cart)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, cart).perform()


    def wait_for_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 40).until(EC.text_to_be_present_in_element(locator, text))