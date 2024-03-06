import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

srvice_obj = Service("C://chromedriver.exe")
d = webdriver.Chrome(service=srvice_obj)
d.implicitly_wait(2)
d.get("https://rahulshettyacademy.com/seleniumPractise/#/")
d.maximize_window()
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg' ,'Strawberry - 1/4 Kg']
actualList =[]

d.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

products = d.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(products)
assert count > 0

for result in products:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert  expectedList == actualList

d.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
d.find_element(By.XPATH,"//button[text()= 'PROCEED TO CHECKOUT']").click()
d.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
d.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait =WebDriverWait(d,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(d.find_element(By.CLASS_NAME,"promoInfo").text)

totals= d.find_elements(By.XPATH,"//tr/td[5]/p")
sum= 0
for price in totals:
    sum =sum + int(price.text)
print("sum=",sum)

totalAmount = int(d.find_element(By.CSS_SELECTOR,".totAmt").text)
print("Total Amount=",totalAmount)
assert sum == totalAmount

discountAmount = float(d.find_element(By.CSS_SELECTOR,".discountAmt").text)
print("Discounted Amount =",discountAmount)

assert discountAmount < totalAmount


