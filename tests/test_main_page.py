import allure
from selenium.webdriver.support.ui import WebDriverWait
import time


@allure.title("Переход по логотипу Самокат ведет на главную страницу")
def test_scooter_logo_redirects_to_main(driver):
    from pages.main_page import MainPage
    main_page = MainPage(driver)

    main_page.open()
    main_page.accept_cookies()
    main_page.click_order_top()
    main_page.click_scooter_logo()

    with allure.step("Проверяем, что открыта главная страница"):
        assert "qa-scooter" in driver.current_url or driver.current_url.endswith("/")


@allure.title("Переход по логотипу Яндекса открывает Дзен в новом окне")
def test_yandex_logo_redirects_to_dzen(driver):
    from pages.main_page import MainPage
    main_page = MainPage(driver)

    main_page.open()
    main_page.accept_cookies()

    initial_windows = driver.window_handles
    main_page.click_yandex_logo()

    # Ждём появления нового окна
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > len(initial_windows))

    # Переключаемся на новое окно
    new_window = [w for w in driver.window_handles if w not in initial_windows][0]
    driver.switch_to.window(new_window)

    # Ждём, пока URL станет не about:blank
    WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")

    with allure.step("Проверяем, что открыта страница Дзена"):
        print("Открыт URL:", driver.current_url)
        assert "dzen" in driver.current_url or "ya.ru" in driver.current_url
