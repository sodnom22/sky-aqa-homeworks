from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://uitestingplayground.com/classattr")

# Ожидаем загрузку страницы
time.sleep(2)

# Находим кнопку по CSS-классу и кликаем на нее
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()

# Подтверждение клика в консоли
print("Кнопка была успешно нажата.")

# Закрываем браузер
time.sleep(2)
driver.quit()
