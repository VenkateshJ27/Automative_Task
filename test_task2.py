from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from conftest import _driver


def test_validate(_driver):
    _driver.find_element("xpath", "//input[@placeholder='Search for products, brands and more']").send_keys("sony watch")
    actions = ActionChains(_driver)
    actions.send_keys(Keys.ENTER).perform()
    click_ = _driver.find_element("xpath","//div[text()='WOKIT Sony Xperia ZL Smartwatch']")
    actions.move_to_element(click_).click()
    actions.perform()
    act_price = _driver.find_element("xpath","(//div[text()='₹2,500'])[1]").text
    # print(act_price)
    handles = _driver.window_handles
    _driver.switch_to.window(handles[1])
    sleep(1)
    _driver.find_element("xpath", "//button[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']").click()
    sleep(2)
    exp_price = _driver.find_element("xpath", "//div[text()='₹2,500']").text
    sleep(1)
    # if act_price == exp_price:
    #     print("cart item is same as item")
    assert act_price == exp_price
    