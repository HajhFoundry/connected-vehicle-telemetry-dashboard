@echo off

echo =====================================
echo STOPPING PLATFORM
echo =====================================

taskkill /F /IM python.exe

echo.
echo All Python processes stopped.

pause