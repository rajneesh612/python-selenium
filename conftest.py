import pytest


@pytest.fixture
def tc_setup():
    print("Launch Browser")
    print("Login")
    print("Browser Product")
    yield
    print("Logoff")
    print("Close Browser")
