from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.storePage import BuyOnStorePage


def test_buy_on_store():
    # Создаем браузер Firefox
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

    buy = BuyOnStorePage(browser)
    buy.authorization_username('standard_user')
    buy.authorization_password('secret_sauce')
    buy.add_to_cart()
    buy.shopping_cart()
    buy.checkout()
    buy.input_first_name('Olga')
    buy.input_last_name('Tsapiro')
    buy.input_postal_code('2403CW')
    buy.button_continue()
    total = buy.summary_total()

    assert total == 'Total: $58.29'

    browser.quit()
