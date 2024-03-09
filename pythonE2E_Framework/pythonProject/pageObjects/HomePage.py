from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, d):
        self.d = d

    shop = (By.CSS_SELECTOR, "a[href*='/angularpractice/shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check_box_click = (By.ID, "exampleCheck1")
    gender = (By.XPATH, "//select[@class='form-control']")
    empStatus = (By.XPATH, "//input[@id='inlineRadio2']")
    submit_Button = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.d.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.d)
        return checkOutPage

    def getName(self):
        return self.d.find_element(*HomePage.name)

    def getEmail(self):
        return self.d.find_element(*HomePage.email)

    def getPassword(self):
        return self.d.find_element(*HomePage.password)

    def checkboxclick(self):
        return self.d.find_element(*HomePage.check_box_click)

    def getGender(self):
        return self.d.find_element(*HomePage.gender)

    def empStatusCheck(self):
        return self.d.find_element(*HomePage.empStatus)

    def submitButton(self):
        return self.d.find_element(*HomePage.submit_Button)

    def successMsg(self):
        return self.d.find_element(*HomePage.success_message)
