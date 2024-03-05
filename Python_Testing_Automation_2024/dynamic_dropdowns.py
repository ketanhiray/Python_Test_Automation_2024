import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("C://chromedriver.exe")

d = webdriver.Chrome(service=service_obj)

d.get("https://rahulshettyacademy.com/dropdownsPractise/")
d.maximize_window()
d.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = d.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for k in countries:
    if k.text == "India":
        k.click()
        break

print(d.find_element(By.ID,"autosuggest").get_attribute("value"))
assert d.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
time.sleep(3)