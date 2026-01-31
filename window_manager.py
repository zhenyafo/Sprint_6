import allure
from pages.base_page import BasePage


class WindowManager(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self):
        main_window = self.get_current_window_handle()
        all_windows = self.get_window_handles()
        for window in all_windows:
            if window != main_window:
                self.switch_to_window(window)
                break
        return self.get_current_url()