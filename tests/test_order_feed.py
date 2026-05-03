import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeed:

    @allure.title("При создании нового заказа счетчик 'Выполнено за всё время' увеличивается")
    @allure.description("Залогиненный пользователь создает заказ, после чего счетчик на странице ленты заказов должен увеличиться.")
    def test_total_orders_counter_increases(self, authorized_main_page):
        main_page = MainPage(authorized_main_page)
        order_feed_page = OrderFeedPage(authorized_main_page)
        
        with allure.step("Открыть ленту заказов и получить текущий счетчик 'Выполнено за всё время'"):
            main_page.click_order_feed_button()  
            total_before = order_feed_page.get_total_orders_count()
            
        with allure.step("Вернуться на главную страницу и создать новый заказ"):
            main_page.click_constructor_button()
            main_page.create_order()  # добавить этот метод в MainPage
            
        with allure.step("Снова открыть ленту заказов и получить обновлённый счетчик"):
            order_feed_page.open_order_feed()
            total_after = order_feed_page.get_total_orders_count()
            
        with allure.step("Проверить, что счетчик увеличился"):
            assert total_after > total_before, \
                f"Счетчик не увеличился: было {total_before}, стало {total_after}"