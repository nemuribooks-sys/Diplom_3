from selenium.webdriver.common.by import By

class BaseLocators:
    """Локаторы для элементов Stellar Burgers"""

    MAIN_PAGE = (By.XPATH, "//h2[text()='Вход']")
    PAGE_TITLE = (By.XPATH, "//p[text()='Лента Заказов']")
    MAIN_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    LOGIN_PAGE_TITLE= (By.XPATH, "//h2[text()='Вход']")
    REGISTRATION_PAGE_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') 
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    EMAIL_INPUT = (By.XPATH, '//div[label[text()="Email"]]//input')
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

    LOGIN_FORM_BUTTON = (By.XPATH, "//button[text()='Войти']")

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_NUMBER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]//h2[contains(@class, 'text_type_digits-large')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    
    # Модальное окно деталей ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_modified')]")
    INGREDIENT_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button")

    # Все ингредиенты
    ALL_INGREDIENTS = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredient__')]")
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")

    INGREDIENTS_BUNS = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")


    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__totalContainer')]")
    
    @staticmethod
    def ingredient_counter_by_name(name):
        return (By.XPATH, f"//h2[text()='{name}']/following-sibling::p[contains(@class, 'counter')]")
    
    @staticmethod
    def ingredient_by_name(name):
        return (By.XPATH, f"//a[.//p[text()='{name}']]")
    
    # ингридиенты

    FLUORESCENT_BUN = (By.XPATH, "//a[.//p[text()='Флюоресцентная булка R2-D3']]")
    KRATORNAYA_BUN = (By.XPATH, "//p[text()='Краторная булка N-200i']")
    SPACE_SAUCE = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']")


