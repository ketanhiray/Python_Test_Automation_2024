import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifylikePresence(self, text):
        element = WebDriverWait(self.d, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )

    def selectOpyionByTest(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)

        return logger
