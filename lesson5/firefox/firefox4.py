from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ожидаем загрузку страницы и модального окна
time.sleep(3)

# Находим кнопку "Close" в модальном окне и кликаем по ней
close_button = driver.find_element(By.CLASS_NAME, "modal-footer").find_element(By.TAG_NAME, "p")
close_button.click()

# Подтверждение в консоли
print("Модальное окно закрыто.")

# Закрываем браузер
time.sleep(2)
driver.quit()
