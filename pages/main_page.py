from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    # Локаторы
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[last()]")
    QUESTION_LIST = (By.CLASS_NAME, "accordion__button")
    ANSWER_TEXT = (By.CLASS_NAME, "accordion__panel")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.open(self.URL)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        if self.is_element_present(self.COOKIE_BUTTON, timeout=5):
            self.click(self.COOKIE_BUTTON)

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_bottom(self):
        self.click(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    @allure.step("Клик по вопросу №{index}")
    def click_question_by_index(self, index):
        self.click_element_by_index(self.QUESTION_LIST, index)

    @allure.step("Получение текста ответа на вопрос №{index}")
    def get_answer_text_by_index(self, index):
        return self.get_text_by_index(self.ANSWER_TEXT, index)
