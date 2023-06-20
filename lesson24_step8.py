from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 14 секунд, пока кнопка не станет кликабельной
book_button = browser.find_element(By.ID, "book")
b = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
book_button.click()

# вычисляем
input1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
input_value = input1.text
y = calc(input_value)
    # вводится ответ
input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
input2.send_keys(y)

# Отправляем заполненную форму
button_submit = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
button_submit.click()

   # успеваем скопировать код за 30 секунд
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()