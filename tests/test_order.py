import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.title("Позитивный сценарий заказа самоката")
@pytest.mark.parametrize("order_button", ["top", "bottom"])
@pytest.mark.parametrize("user_data", [
    {"name": "Иван", "surname": "Иванов", "address": "Москва, Тверская 1", "metro": 0, "phone": "89991234567",
     "date": "30.04.2025", "duration": 1, "color": "black", "comment": "Позвонить за 10 минут"},
    {"name": "Анна", "surname": "Петрова", "address": "СПб, Невский 100", "metro": 3, "phone": "89997654321",
     "date": "01.05.2025", "duration": 2, "color": "grey", "comment": ""}
])
def test_successful_order(driver, order_button, user_data):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Открываем главную страницу"):
        main_page.open()
        main_page.accept_cookies()

    with allure.step(f"Нажимаем кнопку заказа ({order_button})"):
        if order_button == "top":
            main_page.click_order_top()
        else:
            main_page.click_order_bottom()

    with allure.step("Заполняем шаг 1 формы заказа"):
        order_page.fill_step_one(
            user_data["name"], user_data["surname"],
            user_data["address"], user_data["metro"],
            user_data["phone"]
        )

    with allure.step("Заполняем шаг 2 формы заказа"):
        order_page.fill_step_two(
            user_data["date"], user_data["duration"],
            user_data["color"], user_data["comment"]
        )

    with allure.step("Проверяем, что заказ успешно оформлен"):
        assert order_page.is_success_popup_displayed()