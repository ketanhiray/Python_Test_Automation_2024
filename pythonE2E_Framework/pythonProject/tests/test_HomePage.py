import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_FormSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.d)
        homePage.getName().send_keys(getData["name"])
        log.info("Name is :" + getData["name"])
        homePage.getEmail().send_keys(getData["email"])
        log.info("Eamil is :" + getData["email"])
        homePage.getPassword().send_keys("123")
        homePage.checkboxclick().click()
        self.selectOpyionByTest(homePage.getGender(), getData["gender"])
        homePage.empStatusCheck().click()
        homePage.submitButton().click()
        msg = homePage.successMsg().text
        assert ("Success" in msg)
        #assert ("Successooooooo" in msg)
        self.d.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
