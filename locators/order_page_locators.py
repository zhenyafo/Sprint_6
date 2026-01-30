from selenium.webdriver.common.by import By


class OrderPageLocators:
    
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_STATION_ITEM = (By.XPATH, ".//div[@class='select-search__select']//li")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_ITEM = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day--selected')]")
    RENTAL_PERIOD_INPUT = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    COLOR_CHECKBOX_BLACK = (By.ID, "black")
    COLOR_CHECKBOX_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']")

    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_MESSAGE = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")
    VIEW_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")

    RENTAL_PERIODS = {
        "сутки": 0,
        "двое суток": 1,
        "трое суток": 2,
        "четверо суток": 3,
        "пятеро суток": 4,
        "шестеро суток": 5,
        "семеро суток": 6
    } 