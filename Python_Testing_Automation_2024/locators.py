import time

from selenium.webdriver.chrome.service import service, Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("C://chromedriver.exe")

d = webdriver.Chrome(service=service_obj)

d.get("https://rahulshettyacademy.com/angularpractice/")

d.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ketan")
d.find_element(By.NAME, "email").send_keys("test@gmail.com")
d.find_element(By.ID, "exampleInputPassword1").send_keys("123")
d.find_element(By.ID, "exampleCheck1").click()
d.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()


d.find_element(By.XPATH,"//input[@type='submit']").click()
d.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
d.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("testKetan")
message = d.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert "Success" in message
time.sleep(2)
