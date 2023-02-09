import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
from selenium.webdriver.support.ui import Select
import time


def add_account():
    project_root = root_path(ignore_cwd=True)
    # print(project_root)
    driver_path = project_root + "\Drivers\geckodriver.exe"
    # print(driver_path)
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://demo.guru99.com/v4/index.php")

    # enter userID
    userID = driver.find_element(By.NAME, "uid")
    userID.send_keys("mngr477338")

    # enter password
    password = driver.find_element(By.NAME, "password")
    password.send_keys("zanehAj")

    # click login
    login_button = driver.find_element(By.NAME, "btnLogin")
    login_button.click()

    #click new account
    New_account=driver.find_element(By.LINK_TEXT,"New Account")
    New_account.click()
    time.sleep(5)


    #click account type
    #Select(driver.find_element(By.NAME, "selaccount")).select_by_value("Savings")
    Select(driver.find_element(By.NAME, "selaccount")).select_by_visible_text("Current")

    driver.close()

add_account()