@echo off
echo Starting Fake News Detection Application (Optimized)...

echo Starting Backend Server (FastAPI)...
start cmd /k "cd backend && .\venv\Scripts\activate && uvicorn main:app"

echo Starting Frontend Server (Vite)...
start cmd /k "cd frontend && npm run dev"

echo Both servers are starting up. 
echo - The Backend API will be available at: http://127.0.0.1:8000
echo - The Frontend App will be available at: http://localhost:5173
echo.
echo This window will close in 5 seconds...
timeout /t 5 >nul
exit
