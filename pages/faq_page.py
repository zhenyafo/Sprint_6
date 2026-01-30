from locators.faq_page_locators import FAQPageLocators
from .base_page import BasePage


class FAQPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FAQPageLocators()
    
    def scroll_to_faq(self):
        self.scroll_to_element(self.locators.FAQ_SECTION)
    
    def click_question(self, question_index):
        question_locator = self.locators.QUESTION_LOCATORS[question_index]
        self.scroll_to_element(question_locator)
        self.click(question_locator)
    
    def get_answer_text(self, answer_index):
        answer_locator = self.locators.ANSWER_LOCATORS[answer_index]
        return self.get_text(answer_locator)
    
    def is_answer_displayed(self, answer_index):
        answer_locator = self.locators.ANSWER_LOCATORS[answer_index]
        element = self.find_element(answer_locator)
        return element.is_displayed() 