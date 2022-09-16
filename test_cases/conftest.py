import pytest
from selenium import webdriver
from utilities.readProperties import read_config
from fixtures.ui_fixtures import UI
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.ie.service import Service as IEService

config_values = read_config('app_data')


@pytest.fixture()
def ui(browser):
    if browser == "chrome" or browser == "Chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox" or browser == "Firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "ie" or browser == "IE":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.maximize_window()
    driver.get(config_values['baseurl'])
    fixtures_ui = UI(driver)
    return fixtures_ui


@pytest.fixture()
def browser():  # This will return browser value to set up method which is stored in config.ini.
    return read_config('browser')['browser']

