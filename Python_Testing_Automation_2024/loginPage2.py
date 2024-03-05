import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C://chromedriver.exe")

d = webdriver.Chrome(service=service_obj)

d.get("https://rahulshettyacademy.com/loginpagePractise/")
d.maximize_window()
d.find_element(By.CSS_SELECTOR,"#username").send_keys("ketantest@gmail.com")
d.find_element(By.ID,"password").send_keys("Test@123")
d.find_element(By.XPATH,"//span[text()= ' User']").click()
dp = Select(d.find_element(By.XPATH,"//select[@class='form-control']"))
dp.select_by_index(1)


time.sleep(10)