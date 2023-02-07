
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


def set_navigation():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://demo.opencart.com/")
    time.sleep(5)
    driver.get("https://www.google.com/")
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(5)
    driver.refresh()



set_navigation()
