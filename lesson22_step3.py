from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/selects1.html"
    browser.get(link)
    
    a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    a = a_element.text
    b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    b = b_element.text
    sum = int(a) + int(b)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()