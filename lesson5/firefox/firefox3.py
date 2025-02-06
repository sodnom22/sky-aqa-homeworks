from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://uitestingplayground.com/classattr")

# Ожидаем загрузку страницы
time.sleep(2)

# Находим кнопку по CSS-классу (класс у нее может меняться, но всегда содержит 'btn-primary')
button = driver.find_element(By.CLASS_NAME, "btn-primary")

# Кликаем по кнопке
button.click()

# Выводим в консоль подтверждение
print("Синяя кнопка была успешно нажата.")

# Закрываем браузер
time.sleep(2)
driver.quit()
