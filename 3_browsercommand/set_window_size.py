from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def set_window_size():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.set_window_size(500,700)
    driver.get("https://demo.opencart.com/")


set_window_size()
