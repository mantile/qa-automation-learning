@echo off
echo ========================================
echo  Generating Allure Report
echo ========================================

cd /d F:\test\qa-automation-learning

echo [1/4] Removing old report...
if exist allure-report (
    rmdir /s /q allure-report
    echo Old report removed.
)

echo [2/4] Checking for test results...
if not exist allure-results (
    echo ERROR: No test results found in allure-results/
    echo Run tests first: pytest -v --alluredir=allure-results
    pause
    exit /b 1
)

echo [3/4] Generating new report...
allure.cmd generate allure-results -o allure-report

echo [4/4] Opening report...
allure.cmd open allure-report

echo ========================================
echo  Done!
echo ========================================
pause