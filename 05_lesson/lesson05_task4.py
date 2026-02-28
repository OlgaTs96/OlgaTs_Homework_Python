from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")


input_field = driver.find_element(By.CSS_SELECTOR, "#username")
input_field.send_keys("tomsmith")

sleep(3)

input_field = driver.find_element(By.CSS_SELECTOR, "#password")
input_field.send_keys("SuperSecretPassword!")

sleep(3)

login_button = driver.find_element(By.CSS_SELECTOR, "button[class='radius']")
login_button.click()

sleep(3)

driver.quit()
