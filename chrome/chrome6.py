from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле username и вводим значение "tomsmith"
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле password и вводим значение "SuperSecretPassword!"
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Нажимаем кнопку "Login"
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Даем время для загрузки страницы после входа
time.sleep(3)

# Закрываем браузер
driver.quit()
