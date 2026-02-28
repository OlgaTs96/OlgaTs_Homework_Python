import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    yield driver
    driver.quit()


def test_form_validation_and_colors(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'firstName').send_keys('Иван')
    driver.find_element(By.ID, 'lastName').send_keys('Петров')
    driver.find_element(By.ID, 'address').send_keys('Ленина, 55-3')
    driver.find_element(By.ID, 'email').send_keys('test@skypro.com')
    driver.find_element(By.ID, 'phoneNumber').send_keys('+7985899998787')
    driver.find_element(By.ID, 'city').send_keys('Москва')
    driver.find_element(By.ID, 'country').send_keys('Россия')
    driver.find_element(By.ID, 'jobPosition').send_keys('QA')
    driver.find_element(By.ID, 'company').send_keys('SkyPro')

    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    submit_button.click()

    def get_border_color(element):
        return element.value_of_css_property('border-color')

    red_color = 'rgb(255, 0, 0)'
    green_color = 'rgb(0, 128, 0)'

    zip_input = driver.find_element(By.ID, 'zipCode')
    zip_color = get_border_color(zip_input)
    assert zip_color == red_color, f"Expected Zip code to be red, but got {zip_color}"

    other_fields_ids = [
        'firstName', 'lastName', 'address', 'email', 'phoneNumber',
        'city', 'country', 'jobPosition', 'company'
    ]
    for field_id in other_fields_ids:
        element = driver.find_element(By.ID, field_id)
        color = get_border_color(element)
        assert color == green_color, f"Field {field_id} is not green, but {color}"
