import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from flip_credentials import email_id,pass_,phone_


@pytest.fixture
def _driver():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    sleep(2)
    driver.find_element("xpath", "//input[@class = '_2IX_2- VJZDxU']").send_keys(email_id)
    driver.find_element("xpath", "//input[@class = '_2IX_2- _3mctLh VJZDxU']").send_keys(pass_)
    sleep(1)
    driver.find_element("xpath", "//button[@class = '_2KpZ6l _2HKlqd _3AWRsL']").click()
    driver.find_element("xpath", "//input[@class='_2IX_2- VJZDxU']").send_keys(phone_)
    sleep(1)
    driver.find_element("xpath", "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
    sleep(1)
    driver.find_element("xpath", "//input[@class='_2IX_2- _3mctLh VJZDxU']").send_keys(pass_)
    driver.find_element("xpath", "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
    sleep(2)
    yield driver
    actions = ActionChains(driver)
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    res = driver.find_element("xpath", "//div[text()='Venkatesh']")
    actions.move_to_element(res).perform()
    log_out = driver.find_element("xpath", "//div[text()='Logout']")
    actions.move_to_element(log_out).click()
    actions.perform()
    print("successfully logged out")

    