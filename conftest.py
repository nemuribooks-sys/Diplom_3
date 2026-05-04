import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import Credentials
from generators import generate_created_user_dict, generate_user_credentials
from curl import MAIN_SITE
from pages.order_page import OrderPage

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    driver.get(MAIN_SITE)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(MAIN_SITE) 
    order_page = OrderPage(driver)
    order_page.click_personal_account()
    order_page.fill_log_in_form(Credentials.EMAIL, Credentials.PASSWORD)
    return driver

@pytest.fixture
def created_user():
    user_data = generate_created_user_dict()
    response = generate_user_credentials(user_data)
    assert response.status_code == 200, f"Registration failed: {response.text}"
    # Возвращаем данные пользователя и токен, если нужно
    return {
        "user": user_data,
        "accessToken": response.json().get("accessToken"),
        "refreshToken": response.json().get("refreshToken")
        }

@pytest.fixture
def user_login(created_user):
    response = generate_user_credentials()
    assert response.status_code == 200, f"Login failed: {response.text}"
    created_user["accessToken"] = response.json().get("accessToken")
    return created_user