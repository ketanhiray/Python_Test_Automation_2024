import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("C://chromedriver.exe")
d = webdriver.Chrome(service=service_obj)

d.get("https://rahulshettyacademy.com/client/")
d.maximize_window()
#d.find_element(By.ID,"userEmail").send_keys("ketantest@gmail.com")
d.find_element(By.XPATH,"//form/div[1]/input").send_keys("ketantest@gmail.com")
d.find_element(By.XPATH,"//input[@type='password']").send_keys("Test@123")
d.find_element(By.XPATH,"//input[@type='submit']").click()


time.sleep(4)