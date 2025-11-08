Start (activate virtual environment — choose the command that matches your shell):

- PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

- Windows (cmd):
```cmd
.\venv\Scripts\activate
```

- macOS / Linux (bash or zsh):
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the app:
```bash
uvicorn main:app --reload
```

Submission:
Submit the following URL in the TDS assignment portal:

http://localhost:8000/analyze
