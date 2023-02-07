
from selenium import webdriver

def openwebpage_online():

    driver= webdriver.Firefox(executable_path="E:\\Python(BITM)\\geckodriver-v0.32.1-win64\\geckodriver.exe")
    driver.get("https://www.google.com/")
    driver.close()

openwebpage_online()
