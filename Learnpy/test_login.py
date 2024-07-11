import pytest

@pytest.mark.skip
def testlog():
    print("login successful")

@pytest.mark.sanity
def testlogin():
    print("login successful")


@pytest.mark.regression
def testlogoff():
    print("logoff successful")

@pytest.mark.xfail
def testcalculation():
    assert 2+2 == 4