import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    
    