
from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path

class Login_Guru99():
    global driver
    def login_valid(self):
        project_root = root_path(ignore_cwd=True)
        #print(project_root)
        driver_path = project_root + "\Drivers\geckodriver.exe"
        #print(driver_path)
        driver=webdriver.Firefox(executable_path=driver_path)
        driver.get("https://demo.guru99.com/v4/index.php")

        #enter userID
        userID= driver.find_element(By.NAME, "uid")
        userID.send_keys("mngr476842")

        #enter password
        password=driver.find_element(By.NAME, "password")
        password.send_keys("jygYsar")

        #click login
        login_button=driver.find_element(By.NAME, "btnLogin")
        login_button.click()

    def login_invalid(self):
        project_root = root_path(ignore_cwd=True)
        #print(project_root)
        driver_path = project_root + "\Drivers\geckodriver.exe"
        #print(driver_path)
        driver=webdriver.Firefox(executable_path=driver_path)
        driver.get("https://demo.guru99.com/v4/index.php")

        #enter userID
        userID= driver.find_element(By.NAME, "uid")
        userID.send_keys("")

        #enter password
        password=driver.find_element(By.NAME, "password")
        password.send_keys("jygYsar")

        #click login
        login_button=driver.find_element(By.NAME, "btnLogin")
        login_button.click()

        driver.close()

obj=Login_Guru99()
obj.login_valid()
obj.login_invalid()


