from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, ".//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(.//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')])[2]")
    SCOOTER_LOGO = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")