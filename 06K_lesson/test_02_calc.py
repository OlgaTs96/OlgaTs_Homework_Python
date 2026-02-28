import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_slow_calculator_with_wait(driver):
    wait = WebDriverWait(driver, 90)
    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Вводим значение 45 в поле #delay
    delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#delay')))
    delay_input.clear()
    delay_input.send_keys('45')

    # Нажимаем кнопки: 7, +, 8, =
    button_7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']")))
    button_plus = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']")))
    button_8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']")))
    button_equals = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))

    button_7.click()
    button_plus.click()
    button_8.click()
    button_equals.click()

    # Ожидаем результат в элементе с классом 'screen'
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))

    result_element = driver.find_element(By.CLASS_NAME, 'screen')
    result_text = result_element.text.strip()

    assert result_text == '15', f"Результат ожидается 15, но найден: {result_text}"
