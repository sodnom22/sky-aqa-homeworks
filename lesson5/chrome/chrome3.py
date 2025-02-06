from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Запуск WebDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открыть страницу
driver.get("http://uitestingplayground.com/classattr")

# Найти кнопку по CSS-классу
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

# Клик по кнопке
button.click()
print("Кнопка нажата!")

# Небольшая задержка для видимости результата
sleep(2)

# Закрытие браузера
driver.quit()
