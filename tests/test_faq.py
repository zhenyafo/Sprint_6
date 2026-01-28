import pytest
import allure
from pages.main_page import MainPage
from pages.faq_page import FAQPage


@allure.suite("Тесты раздела 'Вопросы о важном'")
class TestFAQ:
    @allure.title("Тест открытия ответов в FAQ")
    @pytest.mark.parametrize("question_index", list(range(8)))
    def test_faq_questions(self, driver, question_index):
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)
            faq_page = FAQPage(driver)
        
        with allure.step("Принятие куки"):
            main_page.accept_cookies()
        
        with allure.step("Скролл к разделу FAQ"):
            faq_page.scroll_to_faq()
        
        with allure.step(f"Клик на вопрос {question_index + 1}"):
            faq_page.click_question(question_index)
        
        with allure.step("Проверка отображения ответа"):
            assert faq_page.is_answer_displayed(question_index), f"Ответ на вопрос {question_index + 1} не отображается"
        
        with allure.step("Проверка текста ответа"):
            actual_answer = faq_page.get_answer_text(question_index)
            expected_answer = faq_page.locators.EXPECTED_ANSWERS[question_index]
            assert actual_answer == expected_answer, \
                f"Неверный текст ответа. Ожидалось: {expected_answer}, Получено: {actual_answer}" 