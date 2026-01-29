from locators.order_page_locators import OrderPageLocators
from .base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()
    
    def fill_first_page(self, name, last_name, address, metro_station, phone):
        self.send_keys(self.locators.NAME_INPUT, name)
        self.send_keys(self.locators.LAST_NAME_INPUT, last_name)
        self.send_keys(self.locators.ADDRESS_INPUT, address)
        
        self.click(self.locators.METRO_STATION_INPUT)
        station_locator = (By.XPATH, f".//div[@class='select-search__select']//li[@data-value]//*[contains(text(), '{metro_station}')]")
        self.click(station_locator)
        
        self.send_keys(self.locators.PHONE_INPUT, phone)
    
    def click_next(self):
        self.click(self.locators.NEXT_BUTTON)
    
    def fill_second_page(self, date, rental_period, color, comment):

        date_input = self.find_element(self.locators.DATE_INPUT)
        self.execute_script("arguments[0].value = arguments[1];", date_input, date)

        self.click(self.locators.RENTAL_PERIOD_INPUT)
        
        self.click(self.locators.RENTAL_PERIOD_INPUT)
        period_options = self.find_elements(self.locators.RENTAL_PERIOD_OPTIONS)
        period_options[self.locators.RENTAL_PERIODS[rental_period]].click()
        
        if color == "black":
            self.click(self.locators.COLOR_CHECKBOX_BLACK)
        elif color == "grey":
            self.click(self.locators.COLOR_CHECKBOX_GREY)
        
        self.send_keys(self.locators.COMMENT_INPUT, comment)
    
    def click_order(self):
        self.click(self.locators.ORDER_BUTTON)
    
    def confirm_order(self):
        self.click(self.locators.CONFIRM_ORDER_BUTTON)
    
    def get_success_message(self):
        return self.get_text(self.locators.SUCCESS_MESSAGE)
    
    def is_success_modal_displayed(self):
        return self.is_element_visible(self.locators.ORDER_MODAL)