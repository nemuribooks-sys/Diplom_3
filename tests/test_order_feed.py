import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderFeed:

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    @allure.description("Авторизованный пользователь создаёт заказ, после этого счётчик на странице ленты заказов должен увеличиться.")
    def test_total_order_counter_increases(self,login):
        driver = login
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Получить текущее значение счётчика 'Выполнено за всё время'"):
            initial_count = order_page.get_total_orders_count()

        # Шаг 2: создать новый заказ
        with allure.step("Создать новый заказ"):
            new_order_number = main_page.create_order()
            allure.attach(str(new_order_number), name="Номер заказа", attachment_type=allure.attachment_type.TEXT)

        # Шаг 3: перейти в ленту заказов и дождаться обновления счётчика
        with allure.step("Открыть ленту заказов"):
            order_page.open_order_feed()

        with allure.step("Ожидать увеличения счётчика на 1"):
            # Ожидаем, что новое значение станет равно initial_count + 1 (таймаут 30 сек)
            for _ in range(30):
                current_count = order_page.get_total_orders_count()
                if current_count == initial_count + 1:
                    break
                import time
                time.sleep(1)
            else:
                raise AssertionError(f"Счётчик не увеличился: было {initial_count}, стало {current_count}")

        # Шаг 4: финальная проверка
        with allure.step("Проверить, что счётчик увеличился ровно на 1"):
            final_count = order_page.get_total_orders_count()
            assert final_count == initial_count + 1, f"Ожидалось {initial_count + 1}, получено {final_count}"