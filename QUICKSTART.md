# Quick Start Guide

Get the TAF framework running in 5 minutes!

## Prerequisites
- Python 3.11+ installed
- Git installed
- Chrome browser (for UI tests)

## Installation

### Windows
```bash
# 1. Clone repository
git clone <repository-url>
cd TAF

# 2. Setup virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install dependencies
pip install -r resources\requirements.txt

# 4. Navigate to tests
cd test_cases

# 5. Run first test
python -m pytest test_api_examples.py -k "test_get_all_users" -v
```

### Linux/Mac
```bash
# 1. Clone repository
git clone <repository-url>
cd TAF

# 2. Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r resources/requirements.txt

# 4. Navigate to tests
cd test_cases

# 5. Run first test
python -m pytest test_api_examples.py -k "test_get_all_users" -v
```

## Success!

You should see:
```
test_api_examples.py::TestAPIExamples::test_get_all_users PASSED [100%]
1 passed in 0.47s
```

## Next Steps

### Run UI Tests
```bash
python -m pytest test_google_search.py -v
```

### Run All Tests
```bash
python -m pytest -v
```

### Configure Settings
Edit `configurations/config.ini`:
- Change browser: `browser = chrome` or `firefox`
- Enable headless mode: `headless = true`
- Change API URL: `base_url = your-api-url`

### View Reports
After running tests, open:
- `reports/report.html` - HTML report (open in browser)
- `reports/junit.xml` - XML report (for CI/CD)

## Troubleshooting

### Virtual environment not activated
Make sure you see `(.venv)` in your terminal prompt.

**Fix:**
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### Import errors
Make sure you're in the virtual environment and dependencies are installed:
```bash
pip install -r resources/requirements.txt
```

### Chrome driver errors
The framework auto-downloads ChromeDriver. Ensure:
- Chrome browser is installed
- Internet connection is active
- Run: `pip install --upgrade webdriver-manager`

## Need More Help?

See the full [README.md](README.md) for:
- Detailed documentation
- API testing guide
- Troubleshooting section
- Creating custom tests
- Advanced configuration

**Happy Testing! 🚀**
