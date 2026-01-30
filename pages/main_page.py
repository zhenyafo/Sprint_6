from locators.main_page_locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
    
    def accept_cookies(self):
        if self.is_element_visible(self.locators.COOKIE_BUTTON):
            self.click(self.locators.COOKIE_BUTTON)
    
    def click_order_button_top(self):
        self.click(self.locators.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.click(self.locators.ORDER_BUTTON_BOTTOM)
    
    def click_scooter_logo(self):
        self.click(self.locators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click(self.locators.YANDEX_LOGO)
    
    def is_main_page(self):
        return "https://qa-scooter.praktikum-services.ru/" in self.get_current_url() 