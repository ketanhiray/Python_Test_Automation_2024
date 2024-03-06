import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C://chromedriver.exe")
d= webdriver.Chrome(service=service_obj)
d.get("https://rahulshettyacademy.com/angularpractice/")
d.implicitly_wait(5)
d.maximize_window()
d.find_element(By.CSS_SELECTOR,"a[href*='/angularpractice/shop']").click()
products = d.find_elements(By.XPATH,"//div[@class='card h-100']")
productName = "Blackberry"
for product in products:
    allProductNames =product.find_element(By.XPATH,"div/h4/a").text
    if allProductNames == productName:
        product.find_element(By.XPATH,"div/button").click()

d.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
#time.sleep(3)

d.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
d.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(d,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
d.find_element(By.LINK_TEXT,"India").click()
d.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
d.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successMsg =d.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you! " in successMsg
d.close()

