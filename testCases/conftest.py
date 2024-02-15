from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Chrome browser is launched")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("The firefox browser is launched")
    else:
        driver = webdriver.Chrome()
        print("Chrome browser is launched")
    return driver

def pytest_addoption(parser):  # This wii get the value from cmd
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the browser value from setup method
    return request.config.getoption("--browser")

# cmd for run (pytest -v -s test_login.py --browser chrome)

#********* Generate Html Report *********

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Shivamjeet",
        "Project Name": "Hybrid Framework Practice",
        "Module": "Customer"
    }
#config.metadata['Project Name'] = 'nop Commerce'
#config.metadata['Module Name'] = 'Customers'
#config.metadata['Tester'] = 'Shivamjeet'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Python_HOME", None)
    metadata.pop("Plugins", None)