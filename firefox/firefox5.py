from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Ожидаем загрузку страницы
time.sleep(2)

# Находим поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Вводим текст "1000"
input_field.send_keys("1000")
time.sleep(1)  # Пауза для визуализации

# Очищаем поле
input_field.clear()
time.sleep(1)

# Вводим текст "999"
input_field.send_keys("999")
time.sleep(2)  # Пауза перед закрытием

# Подтверждение в консоли
print("Текст успешно изменен.")

# Закрываем браузер
driver.quit()
