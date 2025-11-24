Write-Host "Activating virtual environment..." -ForegroundColor Green

& .\venv\Scripts\Activate.ps1

if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to activate virtual environment." -ForegroundColor Red
    exit 1
}

Write-Host "Virtual environment activated successfully!" -ForegroundColor Green

Start-Sleep -Seconds 0.5
# Now run your Python script
python src\main.py