from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service_obj = Service("C://chromedriver.exe")
d = webdriver.Chrome(service=service_obj)
d.implicitly_wait(5)
d.maximize_window()
d.get("https://rahulshettyacademy.com/AutomationPractice/")
#d.execute_script("window.scrollBy(0,document.body.scrollHeight)")

d.execute_script("window.scrollBy(0,500)")
d.get_screenshot_as_file("scrolling.png")
