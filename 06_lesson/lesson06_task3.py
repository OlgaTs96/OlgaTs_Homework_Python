from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Создаем драйвер Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Создаем таймер ожидания
wait = WebDriverWait(driver, 10)

# Ждем пока прогрузится последняя картинка
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))

# Получаем значение атрибута src у третьей картинки
images = driver.find_elements(By.TAG_NAME, "img")
third_image = images[3]
src_value = third_image.get_attribute('src')
print(src_value)

driver.quit()
