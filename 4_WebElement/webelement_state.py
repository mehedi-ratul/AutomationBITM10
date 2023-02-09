import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path


def check_state():
    project_root = root_path(ignore_cwd=True)
    # print(project_root)
    driver_path = project_root + "\Drivers\geckodriver.exe"
    # print(driver_path)
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://demo.guru99.com/v4/index.php")

    userID = driver.find_element(By.NAME, "uid")

    # check display status
    display_status=userID.is_displayed()
    print(display_status)

    #check enable status
    enable_status = userID.is_enabled()
    print(enable_status)

    if display_status==True and enable_status==True:
        userID.send_keys("mngr476842")
        time.sleep(5)

    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(4)

    checkbox2=driver.find_element(By.XPATH, "//form[@id='checkbox']/input[2]")
    checkbox_status=checkbox2.is_selected()

    if checkbox_status==True:
        print("Test passed")
    else:
        print("Test Failed")

    driver.close()


check_state()