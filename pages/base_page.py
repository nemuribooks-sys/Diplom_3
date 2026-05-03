import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page import BaseLocators
from selenium.webdriver.common.action_chains import ActionChains

TIMEOUT = 15

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        """Текущий URL страницы"""
        return self.driver.current_url

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получение текста элемента")
    def get_text_on_element(self, locator, timeout=TIMEOUT):
        """Возвращает текстовое содержимое элемента"""
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute_contains(self, locator, attribute, value, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_clickable(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Проверка отсутствия элемента")
    def is_element_not_present(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self, ingredient_name: str):
        # 1. Найти элемент ингредиента
        ingredient_locator = BaseLocators.ingredient_by_name(ingredient_name)
        ingredient_element = self.wait_for_element_clickable(ingredient_locator)
        
        # 2. Найти зону конструктора (цель перетаскивания)
        target_locator = BaseLocators.CONSTRUCTOR_AREA
        target_element = self.wait_for_element(target_locator)
        
        # 3. Прокрутить до ингредиента (для надёжности)
        self.scroll_to_element(ingredient_locator)
        
        # 4. Выполнить drag-and-drop
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient_element, target_element).perform()

    
    