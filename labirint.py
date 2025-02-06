from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Инициализация WebDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Зайти на Лабиринт
driver.get("https://www.labirint.ru")

# Найти книги по слову Python
search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python", Keys.RETURN)

# Подождать для загрузки результатов
sleep(3)

# Собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product")

# Проверим, сколько книг найдено
print("Найдено книг:", len(books))

# Вывести информацию о книгах
for book in books:
    try:
        title = book.find_element(By.CSS_SELECTOR, ".product-title").text
        author = book.find_element(By.CSS_SELECTOR, ".product-author").text
        price = book.find_element(By.CSS_SELECTOR, ".product-price").text
        print(f"{title} — {author} — {price}")
    except Exception as e:
        print("Ошибка при обработке книги:", e)

driver.quit()






