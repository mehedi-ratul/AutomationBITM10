from selenium import webdriver
import time
class MultipleWindow():
    def switch_window(self):
        driver= webdriver.Edge()
        driver.get("https://google.com")
        print("starting window: "+driver.title)
        time.sleep(3)

        #open a new window
        driver.execute_script("window.open('https://the-internet.herokuapp.com/');")
        time.sleep(5)

        windws= driver.window_handles
        #print(windws)

        #switch to the new window
        driver.switch_to.window(windws[1])
        print("switch to 2nd window: "+driver.title)
        time.sleep(4)


        #switch back to the old window
        driver.switch_to.window(windws[0])
        print("switch to 1st wwindow: "+driver.title)
        time.sleep(3)

        #switch to new window again
        driver.switch_to.window(windws[1])
        print("switch to 2nd window: "+driver.title)
        time.sleep(4)

        driver.quit()

obj=MultipleWindow()
obj.switch_window()