import allure
from pages.main_page import MainPage
from curl import MAIN_SITE

class TestConstructor:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Проверка перехода на «Конструктор»")
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Переходим в личный кабинет"):
            main_page.click_personal_account()

        with allure.step("Переходим на «Конструктор»"):
            main_page.click_constructor_button()

        with allure.step("Проверяем, что произошел переход на главную страницу"):
            assert main_page.url == MAIN_SITE

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Проверка перехода на «Лента заказов»")
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Переходим в личный кабинет"):
            main_page.click_personal_account()

        with allure.step("Переходим на «Лента заказов»"):
            main_page.click_order_feed_button()

        with allure.step("Проверяем, что открыта страница ленты заказов"):
            assert "feed" in driver.current_url

    @allure.title("Клик на ингредиент открывает всплывающее окно")
    @allure.description("При клике на любой ингредиент должно появиться модальное окно с деталями")
    def test_ingredient_click_opens_modal(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Кликнуть на первый ингредиент"):
            main_page.click_first_ingredient()
        
        with allure.step("Проверить, что модальное окно появилось"):
            main_page.is_ingredient_modal_displayed()
            
        with allure.step("Проверить, что заголовок окна не пустой"):
            title = main_page.get_ingredient_modal_title()
            assert title

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.description("При клике на крестик в модальном окне, окно должно закрыться")
    def test_ingredient_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть модальное окно кликом по первому ингредиенту"):
            main_page.click_first_ingredient()
            main_page.is_ingredient_modal_displayed()
            
        with allure.step("Кликнуть по крестику"):
            main_page.close_ingredient_modal()
                
        with allure.step("Проверить, что окно закрылось"):
            assert not main_page.is_ingredient_modal_displayed(), "Окно всё ещё отображается"

    @allure.title("Добавление ингредиента увеличивает счётчик")
    @allure.description("При добавлении ингредиента в заказ (через drag-and-drop) счётчик этого ингредиента должен увеличиться")
    def test_counter_increases(self, driver):
        main_page = MainPage(driver)
        ingredient = "Флюоресцентная булка R2-D3"
        
        with allure.step("Получить начальное значение счётчика"):
            counter_before = main_page.get_ingredient_counter_value(ingredient)
        
        with allure.step("Добавить ингредиент в заказ (drag-and-drop)"):
            main_page.add_ingredient_to_order(ingredient)
            
        with allure.step("Получить значение счётчика после добавления"):
            counter_after = main_page.get_ingredient_counter_value(ingredient)
            
        with allure.step("Проверить, что счётчик увеличился"):
            counter_after > counter_before, f"Было {counter_before}, стало {counter_after}"