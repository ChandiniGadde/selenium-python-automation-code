import pytest


@pytest.fixture()
def setup():
    print("Launch Browser")
    print("Login")
    print("Browse Products")
    yield
    print("Logoff")
    print("closed products")
