from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")

# Ожидаем загрузку страницы
time.sleep(2)

# Находим поле username и вводим "tomsmith"
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле password и вводим "SuperSecretPassword!"
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Находим кнопку "Login" и нажимаем на неё
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Ожидаем завершения входа
time.sleep(3)

# Проверяем успешный вход
success_message = driver.find_element(By.ID, "flash").text
print("Результат авторизации:", success_message)

# Закрываем браузер
driver.quit()
