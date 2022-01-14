import pytest
from selenium import webdriver
from utilities.readProperties import read_config
from libs.ui_fixtures import UI

config_values = read_config('app_data')


@pytest.fixture()
def ui(browser):
    if browser == "chrome" or browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox" or browser == "Firefox":
        driver = webdriver.Firefox()
    elif browser == "ie" or browser == "IE":
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(config_values['baseurl'])
    fixtures_ui = UI(driver)
    return fixtures_ui


@pytest.fixture()
def browser():  # This will return browser value to set up method which is stored in config.ini.
    return read_config('browser')['browser']

