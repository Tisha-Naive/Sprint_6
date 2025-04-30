import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import orders_data

@allure.epic("Оформление заказа")
class TestOrder:

    @allure.title("Успешное оформление заказа")
    @pytest.mark.parametrize("order", orders_data)
    def test_success_order(self, driver, order):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_order_top()

        order_page.fill_step_one(
            name=order["name"],
            surname=order["surname"],
            address=order["address"],
            metro_index=order["metro_index"],
            phone=order["phone"]
        )

        order_page.fill_step_two(
            date=order["date"],
            duration=order["duration"],
            color=order["color"],
            comment=order["comment"]
        )

        assert order_page.is_success_popup_displayed()
