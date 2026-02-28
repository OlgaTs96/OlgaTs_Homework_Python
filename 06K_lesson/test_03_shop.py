import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    # Инициализация Firefox WebDriver с помощью webdriver_manager
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shopping_flow(driver):
    wait = WebDriverWait(driver, 15)

    # 1. Открываем сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавляем товары
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product_name in products:
        # Ищем кнопку "Add to cart" для каждого товара по названию
        button = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']"
        )))
        button.click()

    # 4. Переходим в корзину
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    # 5. Нажимаем Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 6. Заполняем форму
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Ivanov")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # 7. Читаем итоговую сумму
    total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text  # например, "Total: $58.29"
    print("Итоговая сумма:", total_text)

    # 8. Проверка суммы
    import re
    match = re.search(r"\$([0-9,.]+)", total_text)
    total_value = match.group(1) if match else ""
    assert total_value == "58.29", f"Сумма не совпадает! Нашли: {total_value}"
