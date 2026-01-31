import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from window_manager import WindowManager


@allure.suite("Тесты процесса заказа")
class TestOrderFlow:
    ORDER_DATA_TOP_BUTTON = {
        "name": "Иван",
        "last_name": "Иванов",
        "address": "ул. Ленина, д. 1",
        "metro_station": "Сокольники",
        "phone": "+79991234567",
        "date": "2026-01-28", 
        "rental_period": "сутки",
        "color": "black",
        "comment": "Позвонить за час"
    }
    
    ORDER_DATA_BOTTOM_BUTTON = {
        "name": "Мария",
        "last_name": "Петрова",
        "address": "пр. Мира, д. 10",
        "metro_station": "Черкизовская",
        "phone": "+79998765432",
        "date": "2026-01-29", 
        "rental_period": "двое суток",
        "color": "grey",
        "comment": "Оставить у подъезда"
    }
    
    @allure.title("Полный флоу заказа через верхнюю кнопку 'Заказать'")
    def test_order_scooter_top_button(self, driver):
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
        
        with allure.step("Принятие куки"):
            main_page.accept_cookies()
        
        with allure.step("Клик на верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()
        
        with allure.step("Заполнение первой страницы формы"):
            order_page.fill_first_page(
                self.ORDER_DATA_TOP_BUTTON["name"],
                self.ORDER_DATA_TOP_BUTTON["last_name"],
                self.ORDER_DATA_TOP_BUTTON["address"],
                self.ORDER_DATA_TOP_BUTTON["metro_station"],
                self.ORDER_DATA_TOP_BUTTON["phone"]
            )
            order_page.click_next()
        
        with allure.step("Заполнение второй страницы формы"):
            order_page.fill_second_page(
                self.ORDER_DATA_TOP_BUTTON["date"],
                self.ORDER_DATA_TOP_BUTTON["rental_period"],
                self.ORDER_DATA_TOP_BUTTON["color"],
                self.ORDER_DATA_TOP_BUTTON["comment"]
            )
            order_page.click_order()
        
        with allure.step("Подтверждение заказа"):
            order_page.confirm_order()
        
        with allure.step("Проверка успешного создания заказа"):
            assert order_page.is_success_modal_displayed(), "Модальное окно успеха не отображается"
            success_text = order_page.get_success_message()
            assert "Заказ оформлен" in success_text, f"Текст успеха неверный: {success_text}"
    
    @allure.title("Полный флоу заказа через нижнюю кнопку 'Заказать'")
    def test_order_scooter_bottom_button(self, driver):
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
        
        with allure.step("Принятие куки"):
            main_page.accept_cookies()
        
        with allure.step("Клик на нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполнение первой страницы формы"):
            order_page.fill_first_page(
                self.ORDER_DATA_BOTTOM_BUTTON["name"],
                self.ORDER_DATA_BOTTOM_BUTTON["last_name"],
                self.ORDER_DATA_BOTTOM_BUTTON["address"],
                self.ORDER_DATA_BOTTOM_BUTTON["metro_station"],
                self.ORDER_DATA_BOTTOM_BUTTON["phone"]
            )
            order_page.click_next()
        
        with allure.step("Заполнение второй страницы формы"):
            order_page.fill_second_page(
                self.ORDER_DATA_BOTTOM_BUTTON["date"],
                self.ORDER_DATA_BOTTOM_BUTTON["rental_period"],
                self.ORDER_DATA_BOTTOM_BUTTON["color"],
                self.ORDER_DATA_BOTTOM_BUTTON["comment"]
            )
            order_page.click_order()
        
        with allure.step("Подтверждение заказа"):
            order_page.confirm_order()
        
        with allure.step("Проверка успешного создания заказа"):
            assert order_page.is_success_modal_displayed(), "Модальное окно успеха не отображается"
            success_text = order_page.get_success_message()
            assert "Заказ оформлен" in success_text, f"Текст успеха неверный: {success_text}"
    
    @allure.title("Тест перехода на главную через логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)
        
        with allure.step("Принятие куки"):
            main_page.accept_cookies()
        
        with allure.step("Клик на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверка редиректа на главную"):
            assert main_page.is_main_page(), "Не произошел переход на главную страницу Самоката"
    
    @allure.title("Тест перехода на Дзен через логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)
            window_manager = WindowManager(driver)
        
        with allure.step("Принятие куки"):
            main_page.accept_cookies()
        
        with allure.step("Клик на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключение на новую вкладку"):
            new_url = window_manager.switch_to_new_window()
        
        with allure.step("Проверка редиректа на Дзен"):
            assert "dzen.ru" in new_url, f"Не произошел переход на Дзен. Текущий URL: {new_url}"