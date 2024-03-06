import time

from selenium.webdriver.chrome.service import Service

from selenium import  webdriver
from selenium.webdriver.common.by import By

service_obj = Service("C://chromedriver.exe")
d= webdriver.Chrome(service=service_obj)
d.get("https://the-internet.herokuapp.com/iframe")
d.switch_to.frame("mce_0_ifr")
d.find_element(By.ID,"tinymce").clear()
d.find_element(By.ID,"tinymce").send_keys("I'm Ketan and writing in iframes")

d.switch_to.default_content()
text= d.find_element(By.CSS_SELECTOR,"h3").text
actualText="An iFrame containing the TinyMCE WYSIWYG Editor"
print(text)
assert text== actualText
time.sleep(4)
