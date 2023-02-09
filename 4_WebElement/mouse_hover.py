from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
import time
from selenium.webdriver import ActionChains

def mouse_hover_demo():
    project_root = root_path(ignore_cwd=True)
    # print(project_root)
    driver_path = project_root + "\Drivers\geckodriver.exe"
    # print(driver_path)
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://demo.opencart.com/")

    menu = driver.find_element(By.LINK_TEXT, "Desktops")
    actions= ActionChains(driver)
    actions.move_to_element(menu).perform()

    driver.find_element(By.LINK_TEXT,"Mac (1)").click()


mouse_hover_demo()

