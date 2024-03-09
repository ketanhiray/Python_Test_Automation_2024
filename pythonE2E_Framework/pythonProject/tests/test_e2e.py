from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log= self.getLogger()
        homePage = HomePage(self.d)
        checkOutPage = homePage.shopItems()
        log.info("Getting all Card Title")
        checkOutPage.getCardTitle()
        checkOutPage.checkOutItems().click()
        confirmPage = checkOutPage.checkOutButton()
        log.info("Entering Country Name")
        confirmPage.confirmCountry().send_keys("ind")
        self.verifylikePresence("India")
        confirmPage.clickOnDropdwon().click()
        log.info("Text received from dropdown ")
        confirmPage.clickOnCheckBox().click()
        confirmPage.clickOnSubmitButton().click()
        successMsg = confirmPage.successMeassage().text
        assert "Success! Thank you! " in successMsg
        log.info("Test Completed ")
