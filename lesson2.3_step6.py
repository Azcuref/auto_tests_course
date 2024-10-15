from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    button_1 = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    button_1.click()
    tab_1 = browser.window_handles[0]
    tab_2 = browser.window_handles[1]
    browser.switch_to.window(tab_2)
    x = int((browser.find_element(By.ID, "input_value")).text)
    formula = math.log(abs(12 * math.sin(x)))
    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(formula)
    button_2 = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    button_2.click()


finally:
    time.sleep(5)
    browser.quit()
