from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WDW(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.ID, "book")
    button.click()
    x = int((browser.find_element(By.ID, 'input_value')).text)
    formula = math.log(abs(12*math.sin(x)))
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(formula)
    button_2 = WDW(browser, 5).until(EC.element_to_be_clickable((By.ID, 'solve')))
    button_2.click()

finally:
    time.sleep(10)
    browser.quit()
