$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
python -m venv .venv
if ($LASTEXITCODE -ne 0) { throw 'Install Python 3.12 and add it to PATH first.' }
& .\.venv\Scripts\python.exe -m pip install --only-binary=llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw 'Dependency installation failed.' }
& .\.venv\Scripts\python.exe download_model.py
if ($LASTEXITCODE -ne 0) { throw 'Model download failed. Retry with an internet connection.' }
Write-Host 'Setup complete. Double-click Start-Chatbot.cmd.'
