from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")

# Создаем объект ожидания
wait = WebDriverWait(driver, 20)

# Ждем и кликаем по синей кнопке
blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton")))
blue_button.click()

# Ждем появления зеленой плашки
green_panel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

# Получаем текст из зеленой плашки и выводим результат
result_text = green_panel.text
print(result_text)

driver.quit()
