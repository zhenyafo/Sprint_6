from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        element = self.find_element(locator)
        element.click()
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def is_element_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def wait_for_url(self, url):
        return self.wait.until(EC.url_to_be(url))
    
    def get_current_url(self):
        return self.driver.current_url 