from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Ожидаем загрузку страницы
time.sleep(2)

# Находим кнопку по тексту и кликаем на нее
button = driver.find_element(By.XPATH, "//button[contains(text(), 'Button')]")
button.click()

# Подтверждение клика в консоли
print("Кнопка была успешно нажата.")

# Закрываем браузер
time.sleep(2)
driver.quit()
