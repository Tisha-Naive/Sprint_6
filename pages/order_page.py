from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    # Локаторы — Шаг 1
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    METRO_LIST = (By.CLASS_NAME, "select-search__option")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы — Шаг 2
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DURATION_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    DURATION_OPTION = (By.CLASS_NAME, "Dropdown-option")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Локатор — Попап подтверждения
    SUCCESS_POPUP = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @allure.step("Заполнение шага 1 формы заказа")
    def fill_step_one(self, name, surname, address, metro_index, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.click(self.METRO_INPUT)
        self.click_element_by_index(self.METRO_LIST, metro_index)
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнение шага 2 формы заказа")
    def fill_step_two(self, date, duration, color, comment):
        self.send_keys(self.DATE_INPUT, date)
        self.move_and_click_offset()  # чтобы закрыть календарь
        self.click(self.DURATION_DROPDOWN)
        self.click_element_by_index(self.DURATION_OPTION, duration - 1)

        if color == "black":
            self.click(self.COLOR_BLACK)
        elif color == "grey":
            self.click(self.COLOR_GREY)

        self.send_keys(self.COMMENT_INPUT, comment)
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Проверка отображения окна успешного заказа")
    def is_success_popup_displayed(self):
        return self.wait_until_visible(self.SUCCESS_POPUP).is_displayed()
