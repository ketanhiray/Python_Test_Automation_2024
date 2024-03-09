from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage



class CheckOutPage:
    def __init__(self, d):
        self.d = d


    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    allProductTitle = (By.XPATH, "div/h4/a")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    addToCart = (By.XPATH, "div/button")
    checkOutItem = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOutButtonXpath = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.d.find_elements(*CheckOutPage.cardTitle)

    def getProductName(self, card_title, all_product_title, add_to_cart):

        for product in card_title:
            allProductNames = product.find_element(all_product_title).text

            if allProductNames == "Blackberry":
                product.find_element(add_to_cart).click()
        return self.d.find_element(*CheckOutPage.getProductName)

    def checkOutItems(self):
        return self.d.find_element(*CheckOutPage.checkOutItem)

    def checkOutButton(self):
        self.d.find_element(*CheckOutPage.checkOutButtonXpath).click()
        confirmPage = ConfirmPage(self.d)
        return confirmPage