import pytest

from pytestDemo.BassClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_loginData(self,dataload):
        log = self.getLogger()
        log.info(dataload[0])
        log.info(dataload[1])
