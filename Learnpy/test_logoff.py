import pytest


def testlogin():
    print("login successful")

@pytest.mark.sanity
def testlogoff():
    print("logoff successful")

def testcalculation():
      assert 2+2 == 4