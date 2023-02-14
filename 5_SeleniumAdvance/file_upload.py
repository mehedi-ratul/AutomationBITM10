from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class FileUpload():
    def upload(self):
        driver= webdriver.Firefox()
        driver.get("https://the-internet.herokuapp.com/upload")

        choose_file_button=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"file")))
        project_root = root_path(ignore_cwd=True)
        file= project_root+ "\screenshots\Google.png"

        choose_file_button.send_keys(file)

        upload_button=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "file-submit")))
        upload_button.click()

        success_message=WebDriverWait(driver,10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"#content > div > h3"))).text

        actual_msg=success_message
        expected_msg="File Uploaded!"

        try:
            assert expected_msg==actual_msg
            print("uploaded successfully")
        except:
            print("upload failed")

        time.sleep(5)
        driver.close()

obj=FileUpload()
obj.upload()