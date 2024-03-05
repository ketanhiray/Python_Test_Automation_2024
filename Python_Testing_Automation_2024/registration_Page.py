import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C://chromedriver.exe")

d = webdriver.Chrome(service=service_obj)

# d = webdriver.Chrome(Service("C://chromedriver.exe"))

d.get("https://rahulshettyacademy.com/client")
d.maximize_window()

d.find_element(By.CLASS_NAME,"btn1").click()

d.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Ketan")
d.find_element(By.ID,"lastName").send_keys("Test")
d.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("ketantest@gmail.com")
d.find_element(By.CSS_SELECTOR,"#userMobile").send_keys("1234567890")
#dd = Select(d.find_element(By.TAG_NAME,""))
#dd.select_by_index(2)
d.find_element(By.XPATH,"//input[@value='Male']").click()
d.find_element(By.XPATH,"//input[@type='checkbox']").click()
d.find_element(By.ID,"userPassword").send_keys("Test@123")
d.find_element(By.ID,"confirmPassword").send_keys("Test@123")
d.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(10)
