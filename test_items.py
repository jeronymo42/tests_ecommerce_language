from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_step(browser):
    browser.get(link)
    time.sleep(3)
    add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    add_button.click()
    time.sleep(5)