import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

srvice_obj = Service("C://chromedriver.exe")

d = webdriver.Chrome(service=srvice_obj)
d.implicitly_wait(5)
d.get("https://rahulshettyacademy.com/seleniumPractise/#/")
d.maximize_window()
d.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

time.sleep(2)
products = d.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(products)
assert count > 0

for result in products:
    result.find_element(By.XPATH,"div/button").click()


d.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
d.find_element(By.XPATH,"//button[text()= 'PROCEED TO CHECKOUT']").click()
d.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
d.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(d.find_element(By.CLASS_NAME,"promoInfo").text)