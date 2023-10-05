from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_step(browser):
    browser.get(link)
    add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_button
    time.sleep(5)