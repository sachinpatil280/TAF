@echo off
echo Activating virtual environment...
call "%~dp0..\\.venv\\Scripts\\activate.bat"

echo Installing dependencies from requirements.txt...
pip install -r "%~dp0..\\resources\\requirements.txt"

echo.
echo Running Google Search Tests...

SET PATH=%~dp0%..\test_cases\
cd %PATH%

echo.
echo ========================================
echo Running Sanity Tests for Google Search
echo ========================================
python -m pytest test_google_search.py -m sanity

echo.
echo ========================================
echo Running All Google Search Tests  
echo ========================================
python -m pytest test_google_search.py

echo.
echo ========================================
echo Generating Allure Report
echo ========================================
allure serve ..\reports\allure-results