import argparse
import re
from flip_credentials import email_id,pass_,phone_
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("browser", help="Browser")
    args = parser.parse_args()
    if args.browser == './chromedriver':
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.flipkart.com/")
        sleep(2)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element("xpath", "//span[text()='Enter Email/Mobile number']").send_keys(email_id)
        driver.find_element("xpath", "//input[@class = '_2IX_2- _3mctLh VJZDxU']").send_keys(pass_)
        sleep(1)
        driver.find_element("xpath", "//button[@class = '_2KpZ6l _2HKlqd _3AWRsL']").click()
        driver.find_element("xpath", "//input[@class='_2IX_2- VJZDxU']").send_keys(phone_)
        driver.find_element("xpath", "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
        driver.find_element("xpath", "//input[@class='_2IX_2- _3mctLh VJZDxU']").send_keys(pass_)
        driver.find_element("xpath", "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
        sleep(1)
        driver.find_element("xpath", "//input[@placeholder='Search for products, brands and more']").send_keys("sony watch")
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()
        click_ = driver.find_element("xpath","//div[text()='WOKIT Sony Xperia ZL Smartwatch']")
        actions.move_to_element(click_).click()
        actions.perform()
        act_price = driver.find_element("xpath","(//div[text()='₹2,500'])[1]").text
        # print(act_price)
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        sleep(1)
        driver.find_element("xpath", "//button[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']").click()
        sleep(2)
        exp_price = driver.find_element("xpath", "//div[text()='₹2,500']").text
        sleep(1)

        


        #log out code
        driver.switch_to.window(handles[0])
        res = driver.find_element("xpath", "//div[text()='Venkatesh']")
        actions.move_to_element(res).perform()
        log_out = driver.find_element("xpath", "//div[text()='Logout']")
        actions.move_to_element(log_out).click()
        actions.perform()
        
        driver.close()
        print("successfully logged out")



