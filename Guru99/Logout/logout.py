from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
import time


def login_logout():
    project_root = root_path(ignore_cwd=True)
    driver_path = project_root + "\Drivers\geckodriver.exe"
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

    driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(4)
    driver.switch_to.alert.accept()






    driver.close()


login_logout()