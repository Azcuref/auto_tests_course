from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/get_attribute.html'

    browser = webdriver.Chrome() 
    browser.get(link)  

       

    # Элементы страницы
    img_chest = browser.find_element(By.ID, 'treasure') # Находим изображение сундука с сокровищами
    input_answer = browser.find_element(By.ID, 'answer') # Находим текстовое поле
    checkbox_robot = browser.find_element(By.ID, 'robotCheckbox')  # Находим checkbox "I'm the robot'
    radiobutton_robots_rule = browser.find_element(By.ID, 'robotsRule') # Находим radiobutton "Robots rule!"
    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]') # Находим кнопку Submit
    

    # Берем у изображения атрибут valuex
    img_chest_attr_value = img_chest.get_attribute('valuex')
    x = int(img_chest_attr_value)
   

    # Считаем функцию от х
    func = math.log(abs(12*math.sin(x)))
    
    # Вводим полученный ответ в текстовое поле
    input_answer.send_keys(func)

    # Отмечаем checkbox "I'm the robot'
    checkbox_robot.click()

    # Выбираем radiobutton "Robots rule!"
    radiobutton_robots_rule.click()

    # Нажимаем кнопку Submit
    button_submit.click()
    









    '''# считаем значение формулы
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)"""

    """# Ваш код, который заполняет обязательные поля
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    checkbox_robot.click()
    radiobutton_robots_rule = browser.find_element(By.ID, "robotsRule")
    radiobutton_robots_rule.click()
    button_submit = browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
    button_submit.click()"""

    # Находим элемент и проверяем атрибут "checked"
    radiobutton_people_rule = browser.find_element(By.ID, "peopleRule")
    radiobutton_people_checked = radiobutton_people_rule.get_attribute("checked")
    radiobutton_robots_rule = browser.find_element(By.ID, "robotsRule")
    radiobutton_robots_checked = radiobutton_robots_rule.get_attribute('checked')
    print("value of people radiobutton: ", radiobutton_people_checked)
    print("value of robots radiobutton: ", radiobutton_robots_checked)
    # Если атрибут "checked" есть, то тест проходит, иначе выводим сообщение об ошибке в терминале. 
    assert radiobutton_people_checked == "true", "People radio is not selected by default"
    assert radiobutton_robots_checked == "true", "Robots radio is not selected by default"'''

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
