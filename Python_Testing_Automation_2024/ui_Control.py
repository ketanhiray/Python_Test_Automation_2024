import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("C://chromedriver.exe")

d = webdriver.Chrome(service=service_obj)

d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.maximize_window()
checkboxes = d.find_elements(By.XPATH,"//input[@type='checkbox']")
print(checkboxes)

for cb in checkboxes:
    if cb.get_attribute("value")=="option2":
        cb.click()
        assert cb.is_selected()
        break

radio_buttons = d.find_elements(By.XPATH,"//input[@type='radio']")

for rb in radio_buttons:
    if rb.get_attribute("value")=="radio2":
        rb.click()
        assert rb.is_selected()
        break

assert  d.find_element(By.ID,"displayed-text").is_displayed()

d.find_element(By.ID,"hide-textbox").click()

assert not d.find_element(By.ID,"displayed-text").is_displayed()


time.sleep(3)