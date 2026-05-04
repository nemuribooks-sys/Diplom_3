import allure
from pages.base_page import BasePage
from locators.main_page_locators import BaseLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):
    
    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click_on_element(BaseLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        self.click_on_element(BaseLocators.PAGE_TITLE)
    
    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_personal_account(self):
        self.click_on_element(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, ingredient_name):
        ingredient_locator = BaseLocators.ingredient_by_name(ingredient_name)
        self.scroll_to_element(ingredient_locator)
        self.click_on_element(ingredient_locator)

    @allure.step("Кликнуть на первый ингредиент в списке")
    def click_first_ingredient(self):
        self.click_on_element(BaseLocators.FIRST_INGREDIENT)

    @allure.step("Проверить, что модальное окно ингредиента отображается")
    def is_ingredient_modal_displayed(self):
        self.wait_for_element(BaseLocators.INGREDIENT_MODAL)

    @allure.step("Получить заголовок модального окна ингредиента")
    def get_ingredient_modal_title(self):
        return self.get_text_on_element(BaseLocators.INGREDIENT_MODAL_TITLE) 
    
    @allure.step("Закрыть модальное окно кликом на крестик")
    def close_ingredient_modal(self):
        self.click_on_element(BaseLocators.INGREDIENT_CLOSE_BUTTON)
    
    @allure.step("Кликнуть на кнопку 'Войти в аккаунт'")
    def click_login_to_account_button(self):
        self.click_on_element(BaseLocators.LOGIN_TO_ACCOUNT_BUTTON)
    
    @allure.step("Получить заголовок главной страницы")
    def get_main_page_title_text(self):
        return self.get_text_on_element(BaseLocators.MAIN_PAGE_TITLE)
    
    @allure.step("Дождаться кликабельности кнопки 'Конструктор'")
    def wait_for_constructor_clickable(self):
        self.wait_for_element_clickable(BaseLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Открыть карточку инградиента")
    def click_on_card(self, ingredient_number):
        ingredient_locator = BaseLocators.ingredient_counter_by_name(ingredient_number)
        self.scroll_to_element(ingredient_locator)
        self.click_on_element(ingredient_locator)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter_value(self, ingredient_name: str) -> int:
        counter_locator = BaseLocators.ingredient_counter_by_name(ingredient_name)
        try:
            element = self.wait_for_element(counter_locator)
            return int(element.text) if element.text.isdigit() else 0
        except TimeoutException:
            return 0

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self, ingredient_name: str):
        ingredient_locator = BaseLocators.ingredient_by_name(ingredient_name)
        ingredient_element = self.wait_for_element_clickable(ingredient_locator)
        target_locator = BaseLocators.CONSTRUCTOR_AREA
        target_element = self.wait_for_element(target_locator)
        self.scroll_to_element(ingredient_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient_element, target_element).perform()

    @allure.step("Создать новый заказ и получить его номер")
    def create_order(self) -> str:
        self.add_ingredient_to_order("Флюоресцентная булка R2-D3")
        self.add_ingredient_to_order("Соус фирменный Space Sauce")
        self.click_on_element(BaseLocators.ORDER_BUTTON)
        self.wait_for_element(BaseLocators.ORDER_MODAL)
        order_number_element = self.wait_for_element(BaseLocators.ORDER_NUMBER_MODAL)
        order_number = order_number_element.text
        self.click_on_element(BaseLocators.CLOSE_MODAL_BUTTON)
        return order_number