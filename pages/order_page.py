import allure
from locators.order_feed_locators import OrderFeedLocators
from locators.main_page_locators import BaseLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_personal_account(self):
        self.click_on_element(BaseLocators.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step("Заполнить форму авторизации")
    def fill_log_in_form(self, email, password):
        self.send_keys_to_input(BaseLocators.EMAIL_INPUT, email)
        self.send_keys_to_input(BaseLocators.PASSWORD_INPUT, password)
        self.click_login_button()

    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_login_button(self):
        self.click_on_element(BaseLocators.LOGIN_FORM_BUTTON)

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
        self.wait_for_element(OrderFeedLocators.ORDER_IN_PROGRESS)