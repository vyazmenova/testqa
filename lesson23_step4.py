from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    span1 = browser.find_element(By.ID, 'input_value')
    span1 = span1.text

    x = calc(int(span1))
    print(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Отправляем заполненную форму

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)


finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()