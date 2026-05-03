import allure
from pages.base_page import BasePage
from locators.main_page import BaseLocators
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    @allure.step("Получить текст счетчика всех заказов")
    def get_total_orders_count(self) -> int:
        text = self.get_text_on_element(OrderFeedLocators.COUNTER_ALL)
        return int(text) if text.isdigit() else 0

    @allure.step("Получить текст счетчика заказов за сегодня")
    def get_today_orders_count(self) -> int:
        text = self.get_text_on_element(OrderFeedLocators.COUNTER_TODAY)
        return int(text) if text.isdigit() else 0

    @allure.step("Открыть ленту заказов")
    def open_order_feed(self):
        self.click_on_element(OrderFeedLocators.ORDER_FEED_LINK)

    @allure.step("Дождаться появления нового заказа в разделе 'В работе'")
    def wait_for_new_order_in_progress(self, timeout: int = 60):
        self.wait_for_element_clickable(OrderFeedLocators.IN_PROGRESS_ORDERS, timeout)

    @allure.step("Получить номера всех заказов в работе")
    def get_orders_in_progress(self):
        elements = self.driver.find_elements(*OrderFeedLocators.ORDER_IN_PROGRESS)
        return [el.text for el in elements]
    
    @allure.step("Создать новый заказ и получить его номер")
    def create_order(self):
        self.add_ingredient_to_order("Флюоресцентная булка R2-D3")
        self.add_ingredient_to_order("Соус фирменный Space Sauce")
        
        self.click_on_element(BaseLocators.ORDER_BUTTON)
        
        self.wait_for_element(BaseLocators.ORDER_MODAL)
        # Получить номер заказа
        order_number_element = self.wait_for_element(BaseLocators.ORDER_NUMBER_MODAL)
        order_number = order_number_element.text
        # Закрыть окно
        self.click_on_element(BaseLocators.CLOSE_MODAL_BUTTON)
        # Подождать закрытия
        self.wait_for_element(BaseLocators.ORDER_MODAL)
        return order_number