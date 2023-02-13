from selenium import webdriver
import time

driver= webdriver.Firefox()
time.sleep(3)
driver.get("https://google.com")

driver.get_full_page_screenshot_as_file("E:\\Python(BITM)\\AutomationBITM10\\screenshots\\google2.png")

driver.close()