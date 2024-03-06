import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("C://chromedriver.exe")

d = webdriver.Chrome(service=service_obj)

d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.maximize_window()
d.implicitly_wait(3)
action = ActionChains(d)
action.move_to_element(d.find_element(By.ID,"mousehover")).perform()
action.context_click(d.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(d.find_element(By.LINK_TEXT,"Top")).click().perform()
time.sleep(4)