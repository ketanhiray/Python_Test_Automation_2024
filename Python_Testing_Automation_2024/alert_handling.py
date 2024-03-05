import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Ketan"
service_obj = Service("C://chromedriver.exe")
d = webdriver.Chrome(service=service_obj)
d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.maximize_window()
d.find_element(By.ID,"name").send_keys(name)
time.sleep(2)
d.find_element(By.XPATH,"//input[@id ='alertbtn']").click()
alert =d.switch_to.alert
alerttext = alert.text
print(alerttext)

assert name in alerttext
alert.accept()

d.find_element(By.ID,"confirmbtn").click()
cancelAlert = d.switch_to.alert
cancelAlert.dismiss()

time.sleep(3)