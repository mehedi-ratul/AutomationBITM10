from selenium import webdriver

def firefox_launch():
    driver= webdriver.Firefox(executable_path="E:\\Python(BITM)\\geckodriver-v0.32.1-win64\\geckodriver.exe")
    driver.close()


firefox_launch()

