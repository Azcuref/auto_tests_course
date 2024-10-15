from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    obl_input_firstname = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
    obl_input_firstname.send_keys('Ivan')
    obl_input_lastname = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
    obl_input_lastname.send_keys('Petrov')
    obl_input_email = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
    obl_input_email.send_keys('ivanpetrov@test.com')
    button_submit = browser.find_element(By.TAG_NAME, 'button')
    button_submit.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()