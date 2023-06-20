from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Валерия')

    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Красавина')

    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('37373@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))   # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')
    button_file = browser.find_element(By.NAME, 'file')         # добавляем к этому пути имя файла
    button_file.send_keys(file_path)



    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    # Отправляем заполненную форму


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()