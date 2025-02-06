from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Вводим текст "1000"
input_field.send_keys("1000")
time.sleep(1)  # Небольшая пауза для визуализации

# Очищаем поле
input_field.clear()
time.sleep(1)

# Вводим текст "999"
input_field.send_keys("999")
time.sleep(2)  # Пауза перед закрытием

# Закрываем браузер
driver.quit()
