from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")


input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")

sleep(4)

input_field.clear()
input_field.send_keys("Pro")

sleep(4)

driver.quit()
