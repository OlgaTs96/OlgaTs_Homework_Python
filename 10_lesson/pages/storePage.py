from selenium.webdriver.common.by import By


class BuyOnStorePage():
    """
    Класс для автоматизации взаимодействия с сайтом https://www.saucedemo.com/.

    Атрибуты:
        _driver (selenium.webdriver): Экземпляр драйвера Selenium.
    """

    def __init__(self, driver):
        """
        Инициализация страницы магазина.

        Параметры:
            driver (selenium.webdriver): Selenium WebDriver
        Возвращаемое значение:
            None
        """
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')

    def authorization_username(self, term: str) -> None:
        """
        Вводит имя пользователя в поле авторизации.

        Параметры:
            term (str): Имя пользователя для ввода.
        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#user-name').send_keys(term)

    def authorization_password(self, term: str) -> None:
        """
        Вводит пароль и нажимает кнопку входа.

        Параметры:
            term (str): Пароль для ввода.

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#password').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#login-button').click()

    def add_to_cart(self) -> None:
        """
        Добавляет три товара в корзину.

        Параметры:
            отсутствуют (только self).

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#add-to-cart-sauce-labs-bolt-t-shirt'
                                  ).click()
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#add-to-cart-sauce-labs-onesie').click()

    def shopping_cart(self) -> None:
        """
        Переходит в корзину покупок.

        Параметры:
            отсутствуют.

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  'a.shopping_cart_link').click()

    def checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.

        Параметры:
            отсутствуют.

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#checkout').click()

    def input_first_name(self, term: str) -> None:
        """
        Вводит имя покупателя в форму оформления.

        Параметры:
            term (str): Имя для ввода.

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#first-name').send_keys(term)

    def input_last_name(self, term: str) -> None:
        """
        Вводит фамилию покупателя в форму оформления.

        Параметры:
            term (str): Фамилия для ввода.

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#last-name').send_keys(term)

    def input_postal_code(self, term: str) -> None:
        """
        Вводит почтовый индекс в форму оформления.

        Параметры:
            term (str): Почтовый индекс для ввода.

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#postal-code').send_keys(term)

    def button_continue(self) -> None:
        """
        Нажимает кнопку продолжения оформления.

        Параметры:
            отсутствуют.

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  '#continue').click()

    def summary_total(self) -> str:
        """
        Возвращает текст с итоговой суммой заказа.

        Параметры:
            отсутствуют.

        Возвращаемое значение:
            str: Текст с суммой заказа.
        """
        total = self._driver.find_element(By.CSS_SELECTOR,
                                          'div.summary_total_label').text
        return total
