from Automation_Test_Method import Web_Method
import pytest

@pytest.fixture
def web():
    test = Web_Method()
    test.Open_Url("https://www.saucedemo.com/")

    yield test

    test.browser.close()
    test.playwright.stop()