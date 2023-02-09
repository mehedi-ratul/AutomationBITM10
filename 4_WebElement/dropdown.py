from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
from selenium.webdriver.support.ui import Select

class Dropdown():
    def select_options(self):
        project_root = root_path(ignore_cwd=True)
        # print(project_root)
        driver_path = project_root + "\Drivers\geckodriver.exe"
        # print(driver_path)
        driver = webdriver.Firefox(executable_path=driver_path)
        driver.get("https://the-internet.herokuapp.com/dropdown")

        #Select(driver.find_element(By.ID, "dropdown")).select_by_index(1)
        #Select(driver.find_element(By.ID, "dropdown")).select_by_value("2")
        Select(driver.find_element(By.ID, "dropdown")).select_by_visible_text("Option 2")

obj=Dropdown()
obj.select_options()
