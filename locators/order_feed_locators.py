from selenium.webdriver.common.by import By

class OrderFeedLocators:

    PAGE_TITLE = (By.XPATH, "//p[text()='Лента Заказов']")
    COUNTER_ALL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    IN_PROGRESS_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    ORDER_NUMBER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]//h2[contains(@class, 'text_type_digits-large')]")