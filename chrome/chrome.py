from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Инициализация WebDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Найти кнопку "Add Element" и нажать 5 раз
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()
    sleep(0.5)  # Короткая задержка для стабильности

# Найти все кнопки "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Вывести количество кнопок "Delete"
print(f"Количество кнопок 'Delete' на странице: {len(delete_buttons)}")

# Закрыть браузер
driver.quit()
