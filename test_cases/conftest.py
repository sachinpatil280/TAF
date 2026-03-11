import pytest
import os
from selenium import webdriver
from utilities.readProperties import read_config
from fixtures.ui_fixtures import UI
from fixtures.api_fixtures import API
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.ie.service import Service as IEService

config_values = read_config('app_data')
browser_config = read_config('browser')
api_config = read_config('api')


@pytest.fixture()
def ui(browser):
    # Check if headless mode is enabled - prioritize environment variable over config
    headless_env = os.environ.get('HEADLESS', '').lower()
    if headless_env in ('true', '1', 'yes'):
        headless_mode = True
    else:
        headless_mode = browser_config.get('headless', 'false').lower() == 'true'
    
    if browser == "chrome" or browser == "Chrome":
        # Add Chrome options to avoid bot detection
        chrome_options = webdriver.ChromeOptions()
        
        # Headless mode configuration
        if headless_mode:
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")  # Required for CI/CD environments
            chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
            chrome_options.add_argument("--disable-gpu")  # Applicable to some Linux systems
        
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")  # Ensure consistent window size in headless
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser == "firefox" or browser == "Firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "ie" or browser == "IE":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    else:
        chrome_options = webdriver.ChromeOptions()
        
        # Headless mode configuration
        if headless_mode:
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")  # Required for CI/CD environments
            chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
            chrome_options.add_argument("--disable-gpu")  # Applicable to some Linux systems
        
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--window-size=1920,1080")  # Ensure consistent window size in headless
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    if not headless_mode:
        driver.maximize_window()
    driver.get(config_values['baseurl'])
    fixtures_ui = UI(driver)
    return fixtures_ui


@pytest.fixture()
def browser():  # This will return browser value to set up method which is stored in config.ini.
    return read_config('browser')['browser']


@pytest.fixture()
def api():
    """API fixture - provides a configured API client instance"""
    base_url = api_config.get('base_url', '')
    timeout = int(api_config.get('timeout', 30))
    verify_ssl = api_config.get('verify_ssl', 'true').lower() == 'true'
    
    # Create API instance
    api_instance = API(base_url=base_url)
    api_instance.client.timeout = timeout
    api_instance.client.verify_ssl = verify_ssl
    
    yield api_instance
    
    # Cleanup
    api_instance.close()

