from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
import time

def all_alert_demo():
    project_root = root_path(ignore_cwd=True)
    # print(project_root)
    driver_path = project_root + "\Drivers\geckodriver.exe"
    # print(driver_path)
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # click ok button
    driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button").click()
    time.sleep(4)

    driver.switch_to.alert.accept()

    #click cancel button
    driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button").click()
    driver.switch_to.alert.dismiss()

    #promt alart
    driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(3) > button").click()
    driver.switch_to.alert.send_keys("Test Automation")
    time.sleep(2)
    
    driver.switch_to.alert.accept()


all_alert_demo()