from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    URL = "https://qa-scooter.praktikum-services.ru/"

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[last()]")

    # Вопросы и ответы
    QUESTION_LIST = (By.CLASS_NAME, "accordion__button")
    ANSWER_TEXT = (By.CLASS_NAME, "accordion__panel")

    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def click_question_by_index(self, index):
        questions = self.wait.until(EC.presence_of_all_elements_located(self.QUESTION_LIST))
        questions[index].click()

    def get_answer_text_by_index(self, index):
        answers = self.wait.until(EC.presence_of_all_elements_located(self.ANSWER_TEXT))
        return answers[index].text

    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.COOKIE_BUTTON)).click()
        except TimeoutException:
            pass

    def click_order_top(self):
        self.driver.find_element(*self.ORDER_BUTTON_TOP).click()

    def click_order_bottom(self):
        self.driver.find_element(*self.ORDER_BUTTON_BOTTOM).click()

    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()




