from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
from selenium.webdriver.common.keys import Keys
import time


def add_customer_valid():
    project_root = root_path(ignore_cwd=True)
    # print(project_root)
    driver_path = project_root + "\Drivers\geckodriver.exe"
    # print(driver_path)
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://demo.guru99.com/v4/index.php")

    # enter userID
    userID=driver.find_element(By.NAME, "uid")
    userID.send_keys("mngr476842")

    # enter password
    password=driver.find_element(By.NAME, "password")
    password.send_keys("jygYsar")

    # click login
    login_button=driver.find_element(By.NAME, "btnLogin")
    login_button.click()

    #driver.refresh()

    # add new customer
    New_customer=driver.find_element(By.LINK_TEXT, "New Customer")
    New_customer.click()

    #time.sleep(3)

    Customer_name=driver.find_element(By.NAME, "name")
    Customer_name.send_keys("Superman")

    gender_female=driver.find_element(By.CSS_SELECTOR, "body > table > tbody > tr > td > table > tbody > "
                                                       "tr:nth-child(5) > td:nth-child(2) > input["
                                                       "type=radio]:nth-child(2)")
    gender_female.click()

    #time.sleep(3)

    driver.find_element(By.ID, "dob").send_keys("1111")
    driver.find_element(By.ID, "dob").send_keys(Keys.TAB)
    driver.find_element(By.ID, "dob").send_keys("2020")

    address=driver.find_element(By.NAME, "addr")
    address.send_keys("dhaka")

    city=driver.find_element(By.NAME, "city")
    city.send_keys("kishoreganj")

    state=driver.find_element(By.NAME, "state")
    state.send_keys("Bangladesh")

    pin=driver.find_element(By.NAME, "pinno")
    pin.send_keys("121212")

    mobile=driver.find_element(By.NAME, "telephoneno")
    mobile.send_keys("01686557297")

    email_ad=driver.find_element(By.NAME, "emailid")
    email_ad.send_keys("ratul@gmail.com")

    password=driver.find_element(By.NAME,"password")
    password.send_keys("ratul22")


add_customer_valid()

