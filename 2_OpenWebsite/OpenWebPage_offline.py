
from selenium import webdriver

def openwebpage_offline():

    driver= webdriver.Firefox(executable_path="E:\\Python(BITM)\\geckodriver-v0.32.1-win64\\geckodriver.exe")
    driver.get("file:///E:/Python(BITM)/your store.html")
    #driver.close()

openwebpage_offline()
