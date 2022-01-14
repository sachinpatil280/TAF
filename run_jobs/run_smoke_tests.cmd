@echo off
pip install -r "..\resources\requirements.txt"

SET MARKER="smoke"
SET PATH=%~dp0%..\test_cases\

cd %PATH%

pytest -m %MARKER% --alluredir=..\reports\my_allure_results
allure serve ..\reports\my_allure_results