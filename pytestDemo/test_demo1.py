# Important Info:
# 1. Any pytest file should start with test_ or end with _test
# 2. pytest method names should start with "test"
# 3. any code should be wrapped in method only.
# 4. method name should make sense.
# 5. commands in cmd are like: py.test -k {file names you want - without ".py"} -v -s
# 6. to run all tests just use: py.test -v -s
# 7. to run specific test, use py.test <file name>
# 8. it is possible to mark test in order to run specific tests: @pytest.mark.smoke and run like: py.test -m smoke -v -s
# 9. you can skip test using @pytest.mark.skip
# 10. If you want to run a test because it makes some needed calculation but don't want the result: @pytest.mark.xfail
# 11. Datadriven and parametrization can be done with return statements in tuple format
# 12. To generate html report = py.test --html=report.html -v -s

import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 5, "Wrong values"


# @pytest.fixture()
def test_crossBrowser(crossBrowser):
    print(crossBrowser)