from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait_until_clickable(locator).click()

    def send_keys(self, locator, text):
        self.wait_until_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait_until_visible(locator).text

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def move_and_click_offset(self, x_offset=10, y_offset=10):
        self.actions.move_by_offset(x_offset, y_offset).click().perform()
        self.actions.reset_actions()

    def click_element_by_index(self, locator, index):
        self.get_elements(locator)[index].click()

    def get_text_by_index(self, locator, index):
        return self.get_elements(locator)[index].text

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
