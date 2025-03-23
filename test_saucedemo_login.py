import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    """Фикстура инициализирует Chrome и закрывает его после теста."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
 

class TestLogin:
    """Класс без наследования от unittest.TestCase."""

    def test_valid_login(self, driver):
        """
        Тест: проверка входа на https://www.saucedemo.com/ 
        с логином standard_user / secret_sauce.
        """
        driver.get("https://www.saucedemo.com/")
        
        username_field = driver.find_element(By.ID, "user-name")
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        assert driver.current_url == "https://www.saucedemo.com/inventory.html", \
            f"Ожидался переход на inventory.html, но текущий URL: {driver.current_url}"

        
