from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/selects1.html'

try:
    browser.get(link)
    selector1 = Select(browser.find_element(By.ID, 'dropdown'))
    x = browser.find_element(By.ID, 'num1') 
    y = browser.find_element(By.ID, 'num2')
    x = int(x.text)
    y = int(y.text)
    sum = x + y
    selector1.select_by_visible_text(str(sum))
    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button_submit.click()



finally:
    time.sleep(10)
    browser.quit()