from selenium.webdriver.chrome.service import Service
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start--maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("C://chromedriver.exe")
d = webdriver.Chrome(service=service_obj, options=chrome_options)

d.get("https://rahulshettyacademy.com/AutomationPractice/")

print(d.title)
