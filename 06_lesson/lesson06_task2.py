from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

# Создали таймер ожидания
wait = WebDriverWait(driver, 10)

input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("SkyPro")

# Увидели, что текст есть и нажали кнопку
blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton")))
blue_button.click()

# Вывели текст кнопки в консоль
result_text = blue_button.text
print(result_text)
