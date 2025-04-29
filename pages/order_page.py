from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class OrderPage:
    # Шаг 1 — данные пользователя
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    METRO_LIST = (By.CLASS_NAME, "select-search__option")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2 — детали заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DURATION_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    DURATION_OPTION = (By.CLASS_NAME, "Dropdown-option")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Попап успешного заказа
    SUCCESS_POPUP = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_step_one(self, name, surname, address, metro_index, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.METRO_INPUT).click()
        metro_options = self.wait.until(EC.presence_of_all_elements_located(self.METRO_LIST))
        metro_options[metro_index].click()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_step_two(self, date, duration, color, comment):
        self.driver.find_element(*self.DATE_INPUT).send_keys(date)
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()
        self.driver.find_element(*self.DURATION_DROPDOWN).click()
        options = self.wait.until(EC.presence_of_all_elements_located(self.DURATION_OPTION))
        options[duration - 1].click()

        if color == "black":
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*self.COLOR_GREY).click()

        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)
        self.driver.find_element(*self.ORDER_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    def is_success_popup_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_POPUP)).is_displayed()
