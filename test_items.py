from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_card_button(browser):
    browser.get(link)
    add_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(add_button) > 0, 'Элемент не найден!'
    time.sleep(7)