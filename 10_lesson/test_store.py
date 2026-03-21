import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.storePage import BuyOnStorePage


@allure.title("Покупка товара в интернет-магазине")
@allure.description(
    "Тест проверяет процесс авторизации, "
    "добавления товара в корзину, оформления и "
    "проверку итоговой суммы заказа"
)
@allure.feature("Покупки в магазине")
@allure.severity(allure.severity_level.CRITICAL)
def test_buy_on_store():
    with allure.step("Запуск браузера Firefox"):
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    try:
        buy = BuyOnStorePage(browser)

        with allure.step("Авторизация пользователя"):
            buy.authorization_username('standard_user')
            buy.authorization_password('secret_sauce')

        with allure.step("Добавление товара в корзину"):
            buy.add_to_cart()

        with allure.step("Переход в корзину"):
            buy.shopping_cart()

        with allure.step("Оформление заказа"):
            buy.checkout()

        with allure.step("Ввод данных покупателя"):
            buy.input_first_name('Olga')
            buy.input_last_name('Tsapiro')
            buy.input_postal_code('2403CW')

        with allure.step("Продолжить оформление"):
            buy.button_continue()

        with allure.step("Проверка итоговой суммы заказа"):
            total = buy.summary_total()
            assert total == 'Total: $58.29', (
             f"Ожидалась сумма 'Total: $58.29', но получено '{total}'"
            )

    finally:
        with allure.step("Закрытие браузера"):
            browser.quit()
