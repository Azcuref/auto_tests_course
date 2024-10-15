from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    x = int((browser.find_element(By.ID, 'input_value')).text)
    formula = math.log(abs(12*math.sin(x)))
    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(formula)
    checkbox_robot = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_robot.click()
    radio_robots = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robots)
    radio_robots.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button[type = "Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()