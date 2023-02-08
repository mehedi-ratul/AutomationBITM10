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


#add_customer_valid()

def add_customer_invalid_customer_name():
    project_root = root_path(ignore_cwd=True)
    # print(project_root)
    driver_path = project_root + "\Drivers\geckodriver.exe"
    # print(driver_path)
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://demo.guru99.com/v4/index.php")

    # enter userID
    userID = driver.find_element(By.NAME, "uid")
    userID.send_keys("mngr476842")

    # enter password
    password = driver.find_element(By.NAME, "password")
    password.send_keys("jygYsar")

    # click login
    login_button = driver.find_element(By.NAME, "btnLogin")
    login_button.click()

    #time.sleep(5)

    #driver.refresh()

    # add new customer
    New_customer = driver.find_element(By.LINK_TEXT, "New Customer")
    New_customer.click()

    Customer_name = driver.find_element(By.NAME, "name")
    Customer_name.send_keys("")

    gender_female=driver.find_element(By.CSS_SELECTOR, "body > table > tbody > tr > td > table > tbody > "
                                                        "tr:nth-child(5) > td:nth-child(2) > input["
                                                        "type=radio]:nth-child(2)")
    gender_female.click()

    customer_name_error_message_actual=driver.find_element(By.ID, "message").text
    print(customer_name_error_message_actual)


    customer_name_error_message_expected= "Customer name must not be blank"

    try:
        assert customer_name_error_message_expected==customer_name_error_message_actual
        print("assert passed(blank name)")
    except:
        print("Customer name (blank)assert fail")

    #first character space
    Customer_name.send_keys(" superman")

    customer_name_error_message_actual=driver.find_element(By.ID, "message").text
    print(customer_name_error_message_actual)

    customer_name_error_message_expected = "First character can not have space"

    try:
        assert customer_name_error_message_expected == customer_name_error_message_actual
        print("assert passed(first ch space)")
    except:
        print("Customer name (space)assert fail")

    #Number
    Customer_name.send_keys("123456")

    customer_name_error_message_actual = driver.find_element(By.ID, "message").text
    print(customer_name_error_message_actual)


    customer_name_error_message_expected = "Numbers are not allowed"

    try:
        assert customer_name_error_message_expected == customer_name_error_message_actual
        print("assert passed(numbers)")
    except:
        print("Customer name (space)assert fail")

    driver.close()


add_customer_invalid_customer_name()
