
from selenium import webdriver

def openwebpage_local():

    driver= webdriver.Firefox(executable_path="E:\\Python(BITM)\\geckodriver-v0.32.1-win64\\geckodriver.exe")
    driver.get("http://localhost:8080/")
    #driver.close()

openwebpage_local()
