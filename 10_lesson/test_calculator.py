import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage


@allure.title("Тест калькулятора для проверки деления 45 / 3 = 15")
@allure.description(
    "Проверяем правильность результата деления числа 45 на 3 в калькуляторе"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    with allure.step("Запуск браузера Chrome"):
        browser = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
    try:
        calculator = CalculatorPage(browser)
        with allure.step("Ввод числа 45"):
            calculator.delay('45')

        with allure.step("Нажатие кнопки деления и равенства (клик)"):
            calculator.click()

        with allure.step("Получение результата с экрана калькулятора"):
            screen = calculator.screen()

        with allure.step("Проверка, что результат равен '15'"):
            assert screen == '15', f"Ожидалось 15, но получили {screen}"
    finally:
        with allure.step("Закрытие браузера"):
            browser.quit()
