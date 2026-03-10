@echo off
pip install -r "..\resources\requirements.txt"

SET MARKER="smoke"
SET PATH=%~dp0%..\test_cases\

cd %PATH%

pytest -m %MARKER%
allure serve ..\reports\allure-results