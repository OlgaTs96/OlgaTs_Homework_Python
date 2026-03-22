from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CalculatorPage():
    """
    Класс для взаимодействия с калькуляторной страницей по адресу:
    https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html

    Атрибуты:
        _driver (selenium.webdriver): экземпляр драйвера Selenium.
    """

    def __init__(self, driver: str):
        """
        Инициализация страницы калькулятора.

        Параметры:
            driver (str): Selenium WebDriver (например, Chrome/Firefox driver).

        Возвращаемое значение:
            None
        """
        self._driver = driver
        self._driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/'
            'slow-calculator.html')
        self._driver.implicitly_wait(50)

    def delay(self, term: str) -> None:
        """
        Устанавливает задержку выполнения калькулятора.

        Параметры:
            term (str): Значение задержки в миллисекундах,
            устанавливаемое в поле.

        Возвращаемое значение:
            None
        """
        delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(term)

    def click(self) -> None:
        """
        Выполняет последовательность нажатий кнопок калькулятора:
        7 + 8 =

        Параметры:
            отсутствуют (только self)

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.XPATH,
                                  "//*[contains(text(),'7')]").click()
        self._driver.find_element(By.XPATH,
                                  "//*[contains(text(),'+')]").click()
        self._driver.find_element(By.XPATH,
                                  "//*[contains(text(),'8')]").click()
        self._driver.find_element(By.XPATH,
                                  "//*[contains(text(),'=')]").click()

    def screen(self, answer) -> str:
        """
        Возвращает текст с экрана калькулятора после вычисления.
        Возвращаемое значение:
            str: Текст, отображаемый на экране калькулятора.
        """
        screen = self._driver.find_element(By.CSS_SELECTOR, 'div.screen')
        WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), answer)
        )
        return screen.text
