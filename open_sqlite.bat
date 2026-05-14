@echo off
REM Quick launcher for SQLite Browser

echo ========================================
echo SQLite Database Browser Launcher
echo ========================================
echo.
echo Choose an option:
echo   1. Interactive Browser (recommended)
echo   2. Open Users Database
echo   3. Open Predictions Database
echo   4. Open Appointments Database
echo   5. Open Audit Database
echo.

set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    python sqlite_browser.py
) else if "%choice%"=="2" (
    python open_database.py users
) else if "%choice%"=="3" (
    python open_database.py predictions
) else if "%choice%"=="4" (
    python open_database.py appointments
) else if "%choice%"=="5" (
    python open_database.py audit
) else (
    echo Invalid choice!
)

pause
