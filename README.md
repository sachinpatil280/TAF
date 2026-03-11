# Test Automation Framework (TAF)

> **🚀 Production-Ready Test Automation Framework for UI & API Testing**  
> Built with Selenium WebDriver, Pytest, and Python Requests | Page Object Model | Allure Reports | CI/CD Ready

A comprehensive, enterprise-grade test automation framework supporting both **UI** and **API** testing, designed for scalability and maintainability.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/selenium-4.25.0-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/pytest-8.1.1-orange.svg)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Keywords:** `selenium` `pytest` `api-testing` `test-automation` `page-object-model` `allure-reports` `python` `rest-api` `webdriver` `automation-framework`

---

## 📋 Table of Contents
- [Why Use TAF?](#-why-use-taf)
- [Quick Start (5 Minutes)](#-quick-start-5-minutes) - Get running fast! See also: [QUICKSTART.md](QUICKSTART.md)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#getting-started)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Test Reports](#test-reports)
- [API Testing](#api-testing-framework)
- [Creating Custom Tests](#creating-your-own-tests)
- [Useful Commands](#useful-commands-reference)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## 🎯 Why Use TAF?

- **⚡ Fast Setup:** Get started in under 5 minutes
- **🔧 Zero Configuration:** Works out of the box with sensible defaults
- **📊 Beautiful Reports:** Allure and HTML reports with screenshots
- **🎨 Clean Architecture:** Page Object Model for maintainable tests
- **🔄 API & UI Testing:** Unified framework for both testing types
- **🚀 CI/CD Ready:** Easy integration with Jenkins, GitHub Actions, GitLab CI
- **📝 Well Documented:** Comprehensive guides and examples included
- **🤝 Beginner Friendly:** Clear examples and step-by-step tutorials

---
- [API Testing](#api-testing-framework)
- [Creating Custom Tests](#creating-your-own-tests)
- [Useful Commands](#useful-commands-reference)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Features

### UI Testing
- ✅ Selenium WebDriver with Page Object Model (POM)
- ✅ Multiple browser support (Chrome, Firefox, IE)
- ✅ Headless mode configuration
- ✅ Anti-bot detection measures
- ✅ Reusable driver utilities

### API Testing (NEW!)
- ✅ REST API testing with comprehensive validation
- ✅ Support for all HTTP methods (GET, POST, PUT, PATCH, DELETE)
- ✅ Multiple authentication methods (Bearer Token, API Key, Basic Auth)
- ✅ JSON schema validation
- ✅ Response time validation
- ✅ Dynamic test data generation
- ✅ Request/Response logging

### Reporting & CI/CD
- ✅ Allure reports with detailed test results
- ✅ HTML reports with pytest-html
- ✅ JUnit XML reports
- ✅ Configurable test markers (sanity, regression, smoke, api, performance)
- ✅ Parallel test execution support


## Project Structure
Here you can find a short description of main directories, and it's content

- **configurations** - Contains config.ini file for browser settings, application URL, API configuration, and test data
- **fixtures** - Stores pytest fixtures for UI and API testing
  - `ui_fixtures.py` - UI test fixtures with Page Object initialization
  - `api_fixtures.py` - API test fixtures with client initialization
- **page_objects** - Page Object Model classes with locators and page actions
  - `google_search_page.py` - Example Google search page implementation
- **reports** - Auto-generated test reports (HTML, Allure, JUnit XML)
- **resources** - requirements.txt with all required Python packages
- **run_jobs** - Batch scripts to execute test suites
  - `run_google_search_tests.cmd` - Run UI tests
  - `run_api_tests.cmd` - Run API tests
  - `run_smoke_tests.cmd` - Run smoke tests
- **test_cases** - Test case files, conftest.py, and pytest.ini
  - `test_google_search.py` - UI test examples
  - `test_api_examples.py` - API test examples
- **utilities** - Reusable utilities and helper functions
  - `myselenium_driver.py` - Selenium WebDriver wrapper
  - `api_client.py` - REST API client with validation
  - `api_utils.py` - API testing utilities and test data generators
  - `readProperties.py` - Configuration file reader
  - `dbUtils.py` - Database utilities
  - `excelUtils.py` - Excel file operations

---

## 🚀 Quick Start (5 Minutes)

Want to see it in action immediately? Follow these steps:

```bash
# 1. Clone and navigate to the project
git clone <your-repository-url>  # Replace with actual repo URL
cd TAF

# 2. Create virtual environment (Windows)
python -m venv .venv
.venv\Scripts\activate

# For Linux/Mac:
# python3 -m venv .venv
# source .venv/bin/activate

# 3. Install dependencies
pip install -r resources\requirements.txt

# 4. Run your first API test (doesn't require browser)
cd test_cases
python -m pytest test_api_examples.py::TestAPIExamples::test_get_all_users -v

# 5. Run your first UI test (requires Chrome browser)
python -m pytest test_google_search.py::TestGoogleSearch::test_google_search_basic -v
```

**✅ Success! You should see:**
```
test_api_examples.py::TestAPIExamples::test_get_all_users PASSED [100%]
1 passed in 0.47s
```

> **Note:** If you don't see `(.venv)` in your terminal prompt after step 2, the virtual environment is not activated. Repeat the activation command.

## Getting Started

### Prerequisites
- **Python 3.11+** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager - comes with Python)
- **Google Chrome** browser (for UI tests)
- **Git** ([Download Git](https://git-scm.com/downloads))
- **Allure** (optional, for advanced reports) - See [Allure Installation](#allure-installation-optional)

### Installation Steps

#### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd TAF
```

#### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> **Note:** Your terminal prompt should show `(.venv)` when activated

#### 3. Install Dependencies
```bash
pip install -r resources/requirements.txt
```

**Expected output:**
```
Successfully installed selenium-4.25.0 pytest-8.1.1 requests-2.32.3 ...
```

#### 4. Verify Installation
```bash
# Navigate to test_cases folder
cd test_cases

# Run a quick test
python -m pytest test_api_examples.py -k "test_get_all_users" -v
```

If you see `1 passed`, you're all set! ✅

### Configuration

Edit `configurations/config.ini` to customize settings:

```ini
[app_data]
baseurl=https:\\www.google.com

[browser]
browser = chrome          # Options: chrome, firefox, ie
headless = false         # Set to 'true' for headless mode (no browser window)

[api]
base_url = https://jsonplaceholder.typicode.com
timeout = 30             # Request timeout in seconds
verify_ssl = true        # Set to 'false' to disable SSL verification
```

> **Note:** The default configuration works out of the box. No changes needed for initial testing.

## Running Tests

> **Important:** Make sure you're in the `test_cases` folder and virtual environment is activated before running tests.

### UI Tests

#### Run all Google search tests:
```bash
cd test_cases
python -m pytest test_google_search.py -v
```

**Expected output:**
```
test_google_search.py::TestGoogleSearch::test_google_search_basic PASSED [20%]
test_google_search.py::TestGoogleSearch::test_google_im_feeling_lucky PASSED [40%]
...
5 passed in 129.38s
```

#### Run specific test:
```bash
python -m pytest test_google_search.py::TestGoogleSearch::test_google_search_basic -v
```

#### Run with markers:
```bash
# Sanity tests only (faster, essential tests)
python -m pytest test_google_search.py -m sanity -v

# Regression tests only (comprehensive tests)
python -m pytest test_google_search.py -m regression -v
```

#### Run in headless mode:
1. Open `configurations/config.ini`
2. Set `headless = true`
3. Run tests normally - browser won't open

#### Using batch script (Windows):
```bash
# From project root directory
run_jobs\run_google_search_tests.cmd
```

This script will:
- Activate virtual environment
- Install/update dependencies
- Run all Google search tests
- Generate Allure report

### API Tests

#### Run all API tests:
```bash
cd test_cases
python -m pytest test_api_examples.py -m api -v
```

**Expected output:**
```
test_api_examples.py::TestAPIExamples::test_get_all_users PASSED [6%]
test_api_examples.py::TestAPIExamples::test_get_single_user PASSED [13%]
...
15 passed in 2.50s
```

#### Run API sanity tests only:
```bash
python -m pytest test_api_examples.py -m "api and sanity" -v
```

#### Run specific API test:
```bash
python -m pytest test_api_examples.py::TestAPIExamples::test_create_user -v
```

#### Using batch script (Windows):
```bash
# From project root directory
run_jobs\run_api_tests.cmd
```

### Run All Tests

```bash
cd test_cases

# Run all tests (UI + API)
python -m pytest -v

# Run all sanity tests
python -m pytest -m sanity -v

# Run tests in parallel (faster)
python -m pytest -n auto
```

### Quick Examples

#### UI Test Example:
```python
import pytest

class TestGoogleSearch:
    @pytest.mark.sanity
    def test_search(self, ui):
        ui.google_search_page.enter_search_term("Selenium")
        ui.google_search_page.press_enter_to_search()
        ui.google_search_page.wait_for_search_results()
        assert ui.google_search_page.get_search_results_count() > 0
```

#### API Test Example:
```python
import pytest

class TestAPI:
    @pytest.mark.api
    def test_get_users(self, api):
        response = api.client.get('/users')
        api.client.validate_status_code(response, 200)
        api.client.validate_response_time(response, 5.0)
        
        users = response.json()
        assert len(users) > 0
```

## Test Reports

### Automatic Report Generation

Reports are **automatically generated** after every test run in the `reports/` folder:
- **HTML Report**: `reports/report.html` - Open directly in browser
- **JUnit XML**: `reports/junit.xml` - For CI/CD integration
- **Allure Results**: `reports/allure-results/` - For Allure reporting

### View HTML Report

**Windows:**
```bash
# Open in default browser
start reports\report.html
```

**Linux/Mac:**
```bash
# Open in default browser
xdg-open reports/report.html  # Linux
open reports/report.html      # Mac
```

### Generate Allure Report (Optional)

First, install Allure (see [Allure Installation](#allure-installation-optional)).

Then run:
```bash
# From project root
allure serve reports/allure-results
```

The report will automatically open in your browser with:
- ✅ Test execution statistics
- ✅ Pass/fail trends
- ✅ Detailed test steps with logs
- ✅ Request/response logs (for API tests)
- ✅ Screenshots (for UI test failures)
- ✅ Execution timeline

### Allure Installation (Optional)

**Windows (using Scoop):**
```bash
scoop install allure
```

**Mac (using Homebrew):**
```bash
brew install allure
```

**Linux (manual installation):**
```bash
# Download and extract
wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
tar -zxvf allure-2.24.0.tgz
sudo mv allure-2.24.0 /opt/allure

# Add to PATH
echo 'export PATH="/opt/allure/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify installation
allure --version
```

> **Note:** Allure is optional. HTML and JUnit reports work without it.

## API Testing Framework

The framework includes a comprehensive API testing module. For detailed documentation, see [API_TESTING_GUIDE.md](API_TESTING_GUIDE.md)

### Key Features:
- Multiple authentication methods
- Built-in validation (status code, response time, JSON schema)
- Dynamic test data generation
- Request/response logging
- Session management

### Quick Start:
```python
@pytest.mark.api
def test_api_example(api):
    # Make request
    response = api.client.get('/users/1')
    
    # Validate
    api.client.validate_status_code(response, 200)
    api.client.validate_response_contains(response, 'email')
    
    # Use data
    user = response.json()
    assert user['id'] == 1
```

## Creating Your Own Tests

### Adding a New UI Test

1. **Create a new page object** in `page_objects/page_object/`:
```python
# my_page.py
from utilities.myselenium_driver import SeleniumDriver

class MyPage(SeleniumDriver):
    def __init__(self, ui):
        super().__init__(ui)
        self.driver = ui.driver
    
    _login_button = "login-btn"  # locator
    
    def click_login(self):
        self.element_click(self._login_button, "id")
```

2. **Register in fixtures** (`fixtures/ui_fixtures.py`):
```python
from page_objects.page_object.my_page import MyPage

class UI:
    def __init__(self, driver):
        self.driver = driver
        self.my_page = MyPage(self)
```

3. **Create test file** in `test_cases/`:
```python
# test_my_feature.py
import pytest

class TestMyFeature:
    @pytest.mark.sanity
    def test_login(self, ui):
        ui.my_page.click_login()
        assert True
```

### Adding a New API Test

1. **Create test file** in `test_cases/`:
```python
# test_my_api.py
import pytest

class TestMyAPI:
    @pytest.mark.api
    def test_my_endpoint(self, api):
        # Update base URL if needed
        api.set_base_url("https://your-api.com")
        
        # Make request
        response = api.client.get('/your-endpoint')
        
        # Validate
        api.client.validate_status_code(response, 200)
```

2. **Add to config.ini** (optional):
```ini
[api]
base_url = https://your-api.com
timeout = 30
```

3. **Run your test**:
```bash
python -m pytest test_my_api.py -v
```

## Useful Commands Reference

### Virtual Environment
```bash
# Activate
.venv\Scripts\activate              # Windows
source .venv/bin/activate           # Linux/Mac

# Deactivate
deactivate

# Recreate
rmdir /s .venv                      # Windows
rm -rf .venv                        # Linux/Mac
python -m venv .venv
```

### Running Tests
```bash
# Single test file
python -m pytest test_api_examples.py -v

# Specific test
python -m pytest test_api_examples.py::TestAPIExamples::test_get_all_users -v

# By marker
python -m pytest -m sanity -v
python -m pytest -m "api and sanity" -v

# With output
python -m pytest test_api_examples.py -v -s

# Parallel execution
python -m pytest -n auto

# Stop on first failure
python -m pytest -x

# Last failed tests only
python -m pytest --lf
```

### Reports
```bash
# Generate reports
python -m pytest --html=reports/report.html --alluredir=reports/allure-results

# View Allure report
allure serve reports/allure-results

# Open HTML report (Windows)
start reports\report.html
```

### Cleanup
```bash
# Clear cache
pytest --cache-clear

# Remove reports
rm -rf reports/*              # Linux/Mac
del /q reports\*              # Windows

# Remove Python cache
find . -type d -name __pycache__ -exec rm -rf {} +    # Linux/Mac
```

## Project Features Summary

### Framework Design
- ✅ Page Object Model (POM) for UI tests
- ✅ Reusable API client for REST testing
- ✅ Fixture-based test setup
- ✅ Configuration-driven execution

### Test Management
- ✅ Pytest markers for test organization
- ✅ Parallel execution support (pytest-xdist)
- ✅ Data-driven testing capability
- ✅ Custom test data generators

### Validation & Reporting
- ✅ Multiple assertion methods
- ✅ JSON schema validation
- ✅ Response time monitoring
- ✅ Comprehensive test reports

## Troubleshooting

### Common Issues and Solutions

#### 1. "Python not found" or "pip not found"
**Problem:** Python is not installed or not in PATH.

**Solution:**
- Download Python from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"
- Restart terminal after installation
- Verify: `python --version` and `pip --version`

#### 2. "No module named 'selenium'" or similar import errors
**Problem:** Dependencies not installed or wrong virtual environment.

**Solution:**
```bash
# Make sure virtual environment is activated (you should see (.venv) in prompt)
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r resources/requirements.txt
```

#### 3. "ChromeDriver not found" or browser errors
**Problem:** WebDriver not properly installed.

**Solution:**
- The framework uses `webdriver-manager` which auto-downloads drivers
- Ensure Chrome browser is installed
- Check internet connection (needed for first-time driver download)
- If issues persist, manually install ChromeDriver:
  ```bash
  pip install --upgrade webdriver-manager
  ```

#### 4. Tests fail with "element not found" or timeout errors
**Problem:** Page load timing or bot detection.

**Solution:**
- Enable headless mode: Set `headless = false` in config.ini
- Increase timeout in test if needed
- Check internet connection
- Some websites may block automation - this is expected behavior

#### 5. "Permission denied" errors on Windows
**Problem:** Script execution policy.

**Solution:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 6. API tests fail with connection errors
**Problem:** Network issues or API endpoint down.

**Solution:**
- Check internet connection
- Verify API base_url in config.ini is correct
- Try accessing the API URL in browser: https://jsonplaceholder.typicode.com/users
- Set `verify_ssl = false` if using self-signed certificates (development only)

#### 7. Virtual environment activation fails
**Problem:** Activation script not found or wrong command.

**Solution:**

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

#### 8. "pytest: command not found"
**Problem:** pytest not installed or not in PATH.

**Solution:**
```bash
# Ensure virtual environment is activated
pip install pytest

# Or use python -m pytest instead
python -m pytest test_api_examples.py -v
```

#### 9. Reports not generated
**Problem:** Reports folder permissions or configuration issue.

**Solution:**
- Check `reports/` folder exists and is writable
- Verify pytest.ini has correct paths
- Run with explicit report generation:
  ```bash
  python -m pytest --html=reports/report.html --alluredir=reports/allure-results
  ```

#### 10. Tests run but all fail immediately
**Problem:** Configuration file not found or incorrect format.

**Solution:**
- Verify `configurations/config.ini` exists
- Check file encoding (should be UTF-8)
- Ensure no syntax errors in config.ini
- Verify section headers: `[app_data]`, `[browser]`, `[api]`

### Still Having Issues?

1. **Check Python version:** `python --version` (should be 3.11+)
2. **Check if virtual environment is active:** Look for `(.venv)` in terminal prompt
3. **Try clean reinstall:**
   ```bash
   # Remove virtual environment
   rmdir /s .venv  # Windows
   rm -rf .venv    # Linux/Mac
   
   # Recreate and reinstall
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r resources/requirements.txt
   ```
4. **Check logs:** Test output shows detailed error messages
5. **Run single test with verbose output:**
   ```bash
   python -m pytest test_api_examples.py::TestAPIExamples::test_get_all_users -v -s
   ```

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

### Ways to Contribute
1. 🐛 **Report bugs** - [Open an issue](https://github.com/YOUR-USERNAME/TAF/issues/new?template=bug_report.md)
2. 💡 **Suggest features** - [Request a feature](https://github.com/YOUR-USERNAME/TAF/issues/new?template=feature_request.md)
3. 📝 **Improve documentation** - Fix typos, add examples
4. 🧪 **Add tests** - Create new test cases
5. 🔧 **Add page objects** - Expand UI test coverage
6. 🚀 **Add API endpoints** - Create new API test examples

### Quick Start for Contributors
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests to ensure nothing breaks: `python -m pytest`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Add docstrings to functions
- Use meaningful variable names
- Keep page objects in separate files
- Add comments for complex logic

## Frequently Asked Questions (FAQ)

**Q: Can I use this for my own project?**  
A: Yes! This framework is open source and free to use for any project.

**Q: Do I need Allure for reports?**  
A: No, Allure is optional. HTML and JUnit reports work without it.

**Q: Can I test mobile applications?**  
A: Currently supports web UI and REST API testing. Mobile support can be added with Appium.

**Q: What if my application uses a different browser?**  
A: Update `config.ini` to change browser. Chrome, Firefox, and IE are pre-configured.

**Q: How do I test APIs with authentication?**  
A: See [API_TESTING_GUIDE.md](API_TESTING_GUIDE.md) for authentication examples.

**Q: Can I run tests in CI/CD?**  
A: Yes! The framework generates JUnit XML reports compatible with Jenkins, GitLab CI, GitHub Actions, etc.

**Q: Tests are too slow. How to speed up?**  
A: Run tests in parallel: `python -m pytest -n auto`

**Q: Can I test against different environments (dev, staging, prod)?**  
A: Yes! Update `base_url` in config.ini or create multiple config files.

## Support

Need help? Here are your options:

1. **Check Documentation**
   - [README.md](README.md) - Main documentation
   - [API_TESTING_GUIDE.md](API_TESTING_GUIDE.md) - API testing details
   - [Troubleshooting](#troubleshooting) - Common issues

2. **Search Issues**
   - Check if your question was already answered in GitHub Issues

3. **Ask for Help**
   - Open a new issue with:
     - Clear description of the problem
     - Steps to reproduce
     - Error messages/screenshots
     - Your environment (OS, Python version)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Additional Documentation

- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community standards
- [Security Policy](SECURITY.md) - Reporting vulnerabilities
- [Changelog](CHANGELOG.md) - Version history
- [Reachability Guide](REACHABILITY_GUIDE.md) - Make your repo more discoverable

---

**Made with ❤️ by the TAF Team**

*Happy Testing! 🚀*


