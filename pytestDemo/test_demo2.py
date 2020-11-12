import pytest

@pytest.mark.smoke
# @pytest.mark.skip
@pytest.mark.xfail
def test_firstProgram_1():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings don't match"

def test_firstCreditCard():
    print("Welcome to my new world")


