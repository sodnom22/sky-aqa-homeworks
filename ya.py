from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация WebDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открытие страниц
driver.get("https://ya.ru")
driver.refresh()
driver.get("https://vk.com")

# Навигация вперед-назад
for x in range(1, 10):
    driver.back()
driver.forward()

# Установка размера окна
driver.set_window_size(640, 460)

driver.get("https://ya.ru")  # Открытие страницы

driver.get("https://vk.com")  # Переход на следующую страницу

driver.set_window_size(640, 460)  # Смена размера окна

# Управление окном браузера
driver.maximize_window()  # Открыть окно на весь экран
driver.minimize_window()  # Свернуть окно браузера
driver.fullscreen_window()  # Развернуть окно в полноэкранный режим

sleep(50)  # Пауза перед закрытием

driver.save_screenshot("ya.png")  # Сохранит скриншот в текущей директории

driver.quit()  # Закрытие браузера



