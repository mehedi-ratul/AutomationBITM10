
from selenium import webdriver
import time

driver= webdriver.Firefox()
time.sleep(5)
driver.get("https://google.com")
driver.close()