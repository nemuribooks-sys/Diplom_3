import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from generators import generate_created_user_dict, generate_user_credentials
from curl import MAIN_SITE

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    driver.get(MAIN_SITE)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def created_user():
    user_data = generate_created_user_dict()
    response = generate_user_credentials()
    assert response.status_code == 200
    user_data["accessToken"] = response.json().get("accessToken")
    yield user_data
    user_data["accessToken"]

@pytest.fixture(scope="function")
def user_login(created_user):
    response = generate_user_credentials()
    assert response.status_code == 200
    access_token = response.json().get("accessToken")
    created_user["accessToken"] = access_token
    return created_user

