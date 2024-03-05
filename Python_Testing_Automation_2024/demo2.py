import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

#d = webdriver.Chrome()
service_obj = Service("C://geckodriver.exe")
d = webdriver.Firefox(service=service_obj)


d.get("https://rahulshettyacademy.com/")

d.maximize_window()
print(d.title)
print(d.current_url)

time.sleep(2)
