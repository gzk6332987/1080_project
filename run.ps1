# run.ps1

Write-Host "Activating virtual environment..." -ForegroundColor Green

# Install virtualenv if not present
python -m pip install virtualenv

# Create virtual environment
python -m virtualenv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to activate virtual environment." -ForegroundColor Red
    exit 1
}

Write-Host "Virtual environment activated successfully!" -ForegroundColor Green

Start-Sleep -Milliseconds 500

# Now run your Python script
python src\main.py

# Keep window open if running by double-clicking
if ($Host.Name -eq "ConsoleHost") {
    Write-Host "Press any key to continue..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}