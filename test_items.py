from selenium.webdriver.common.by import By
import time


def test_button_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    assert button, 'button not found'
