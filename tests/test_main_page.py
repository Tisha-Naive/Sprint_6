import allure
from pages.main_page import MainPage

@allure.epic("Главная страница")
class TestMainPage:

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_order_top()
        main_page.click_scooter_logo()
        assert main_page.URL in driver.current_url

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        assert "dzen.ru" in driver.current_url
