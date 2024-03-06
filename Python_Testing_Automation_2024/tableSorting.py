from selenium.webdriver.chrome.service import Service
from selenium import  webdriver
from selenium.webdriver.common.by import By

sortedList =[]
service_obj = Service("C://chromedriver.exe")
d =webdriver.Chrome(service=service_obj)

d.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
d.maximize_window()
d.implicitly_wait(5)

d.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
vegElements =d.find_elements(By.XPATH,"//tr/td[1]")

for ele in vegElements:
    sortedList.append(ele.text)

originarlList = sortedList.copy()
sortedList.sort()

assert sortedList == originarlList
