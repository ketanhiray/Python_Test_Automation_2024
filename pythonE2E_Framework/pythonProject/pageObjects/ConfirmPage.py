from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:
    def __init__(self, d):
        self.d = d

    enterCountry = (By.ID, "country")
    display_country = (By.LINK_TEXT, "India")
    clickOnOption = (By.LINK_TEXT, "India")
    click_CheckBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_button = (By.CSS_SELECTOR, "[type='submit']")
    success_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def confirmCountry(self):
        return self.d.find_element(*ConfirmPage.enterCountry)

    def clickOnDropdwon(self):
        return self.d.find_element(*ConfirmPage.clickOnOption)

    def clickOnCheckBox(self):
        return self.d.find_element(*ConfirmPage.click_CheckBox)

    def clickOnSubmitButton(self):
        return self.d.find_element(*ConfirmPage.submit_button)

    def successMeassage(self):
        return self.d.find_element(*ConfirmPage.success_msg)
