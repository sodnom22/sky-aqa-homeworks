from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Указываем путь к Firefox WebDriver (если он не добавлен в PATH)
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Находим кнопку "Add Element"
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

# Кликаем по кнопке 5 раз
for _ in range(5):
    add_button.click()
    time.sleep(0.5)  # Пауза для визуализации

# Собираем все кнопки "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Выводим количество кнопок "Delete"
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

# Закрываем браузер
driver.quit()
