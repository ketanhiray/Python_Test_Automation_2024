from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.d)
        homePage.shopItems().click()

        # products = self.d.find_elements(By.XPATH, "//div[@class='card h-100']")

        checkOutPage = CheckOutPage(self.d)
        card = checkOutPage.getCardTitle()


        #for product in card:
            #allProductNames = product.find_element(By.XPATH, "div/h4/a").text
            #textExtract = checkOutPage.getProductName()
            #allProductNames = product.textExtract.text
            #if allProductNames == "Blackberry":
                #product.find_element(By.XPATH, "div/button").click()

        self.d.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        # time.sleep(3)

        self.d.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.d.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.d, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.d.find_element(By.LINK_TEXT, "India").click()
        self.d.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.d.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successMsg = self.d.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        assert "Success! Thank you! " in successMsg
