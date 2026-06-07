@echo off

echo =====================================
echo CONNECTED VEHICLE TELEMETRY PLATFORM
echo =====================================

echo.
echo Starting FastAPI Backend...
start cmd /k "uvicorn backend.main:app --reload"

timeout /t 5

echo.
echo Starting Vehicle Simulator...
start cmd /k "python simulator\vehicle_simulator.py"

timeout /t 5

echo.
echo Starting Streamlit Dashboard...
start cmd /k "streamlit run dashboard\streamlit_app.py"

echo.
echo =====================================
echo PLATFORM STARTED
echo =====================================

pause