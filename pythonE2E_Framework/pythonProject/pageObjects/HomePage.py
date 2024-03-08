from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, d):
        self.d = d

    shop =(By.CSS_SELECTOR,"a[href*='/angularpractice/shop']")

    def shopItems(self):
        return self.d.find_element(*HomePage.shop)