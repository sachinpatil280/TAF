# Test Automation Framework

This is my first test automation framework based on Selenium-Webdriver with Python.


## Project Structure
Here you can find a short description of main directories, and it's content

- configurations - This contains config.ini file, where user can store data like, browser type, application URL and common test data.
- logs - This folder will be used for creation of logs.
- page_objects - In this folder, user can write the page object model stuff and storing code of each application page.
- reports - In this folder, reports will be created.
- resources - In this folder, requirements.txt file is stored.
- run_jobs - Scripts are saved to run test cases with specific marker.
- screenshots - On failure, screenshot captured can be stored here. (code snippet: self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png"))
- test_cases - This folder will consist of test case files.
- test_data - All required test data can be stored in this folder.
- utilities - All common/reusable codes are stored in this folder.


## Project Features
- framework follows Page Object Model
- the ability to easily generate legible and attractive test reports using allure reports.
- tests can be run on popular browsers - Chrome and Firefox are preconfigured in DriverFactory class and both can be selected in [conftest.py](test_cases/conftest.py), e.g.
```
@pytest.fixture()
def setup(browser):
    if browser == "chrome" or browser == "Chrome":
        driver = webdriver.Chrome()
```


## Getting Started

To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone repository. You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

```
$ pip install -r requirements.txt
```

## Run Automated Tests

To run selected test you need to set pytest as default test runner in Pycharm first
```
File > Settings > Tools > Python Integrated Tools > Testing > Default test runner: pytest
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow. 

## Generate Test Report
Move to test_cases folder and execute below commands:

Run 1st command to run test cases and use allure to generate files for raw report creation.
Run 2nd command to generate allure reports.

```
1. pytest --alluredir=../reports/my_allure_results
2. allure serve ../reports/my_allure_results
```
Report generated can be viewed in any browser.

