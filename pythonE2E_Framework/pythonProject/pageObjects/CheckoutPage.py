from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, d):
        self.d = d

    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    allProductTitle = (By.XPATH, "div/h4/a")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    addToCart = (By.XPATH, "div/button")

    def getCardTitle(self):
        return self.d.find_elements(*CheckOutPage.cardTitle)

    def getProductName(self, card_title, all_product_title, add_to_cart):

        for product in card_title:

            allProductNames = product.find_element(all_product_title).text
            if allProductNames == "Blackberry":
                product.find_element(add_to_cart).click()
        return self.d.find_element(*CheckOutPage.allProductNames)
