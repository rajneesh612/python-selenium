import pytest


@pytest.fixture(autouse=True)
def tc_setup():
    print("Launch Browser")
    print("Login")
    print("Browser Product")
    yield
    print("Logoff")
    print("Close Browser")
