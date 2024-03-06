from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj= Service("C://chromedriver.exe")
d= webdriver.Chrome(service=service_obj)

d.get("https://the-internet.herokuapp.com/windows")
d.find_element(By.LINK_TEXT,"Click Here").click()

windowsOpend = d.window_handles
d.switch_to.window(windowsOpend[1])

print(d.find_element(By.TAG_NAME,"h3").text)
d.close()
d.switch_to.window(windowsOpend[0])

print(d.find_element(By.TAG_NAME,"h3").text)
text= "Opening a new window"
newText = d.find_element(By.TAG_NAME,"h3").text
assert text == newText
