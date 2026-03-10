@echo off
echo Activating virtual environment...
call "%~dp0..\\.venv\\Scripts\\activate.bat"

echo Installing dependencies from requirements.txt...
pip install -r "%~dp0..\\resources\\requirements.txt"

echo.
echo Running API Tests...

SET PATH=%~dp0%..\test_cases\
cd %PATH%

echo.
echo ========================================
echo Running Sanity API Tests
echo ========================================
python -m pytest test_api_examples.py -m "api and sanity"

echo.
echo ========================================
echo Running All API Tests
echo ========================================
python -m pytest test_api_examples.py -m api

echo.
echo ========================================
echo Generating Allure Report
echo ========================================
allure serve ..\reports\allure-results

pause
