@echo off
pip install -r "../resources/requirements.txt"

MARKER="sanity"

dir=$PWD
cd "$dir"/../test_cases || exit

pytest -m $MARKER --alluredir=../reports/my_allure_results
allure serve ../reports/my_allure_results
