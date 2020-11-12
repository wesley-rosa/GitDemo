import pytest
from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        # print(dataLoad[0])
        # print(dataLoad[1])
        log = self.getLogger()
        log.info(dataLoad[0])
        log.critical(dataLoad[1])

