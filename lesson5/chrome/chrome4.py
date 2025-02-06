from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск WebDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ожидание появления модального окна
wait = WebDriverWait(driver, 10)
modal = wait.until(EC.presence_of_element_located((By.ID, "modal")))

# Найти кнопку "Close" и нажать
close_button = modal.find_element(By.XPATH, "//div[@class='modal-footer']/p")
close_button.click()

print("Модальное окно закрыто!")

# Закрытие браузера
driver.quit()
