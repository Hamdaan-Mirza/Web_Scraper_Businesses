# Web_Scraper_Businesses
# Lead Generation (Google Maps)

This script collects basic business leads (name, website, phone) from Google Maps search results.

## Prerequisites
- Windows PowerShell
- Python 3.13 (or compatible)
- Chrome installed

## Setup
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
# If venv is activated
pip install -r requirements.txt

# If pip isn't recognized, use the venv Python directly
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

3. (Optional) Verify local ChromeDriver if you use the bundled binary:

```powershell
& .\chromedriver.exe --version
```

Note: With Selenium 4.6+, Selenium Manager auto-downloads/selects a driver. The script prefers Selenium Manager and falls back to `chromedriver.exe` in this folder if needed.

## Configuration
Adjust these values in `script.py`:
- `SEARCH_QUERY`: Your target search, e.g., "roofing companies South Africa"
- `OUTPUT_FILE`: CSV output filename
- `SCROLL_PAUSES`: Number of scroll iterations to load more results

## Run
From this folder:

```powershell
python script.py
```

CSV will be saved to `OUTPUT_FILE` with columns: `Business_Name`, `Website_URL`, `Phone_Number`.

## Notes
- Respect website terms of service and robots policies. Automated scraping of Google Maps may violate their TOS; use responsibly.
- If headless runs are preferred, you can add `options.add_argument('--headless=new')` in `script.py` where the Chrome options are created.
- If Selenium Manager fails due to network restrictions, ensure `chromedriver.exe` matches the installed Chrome version; otherwise update Chrome or download a matching driver.

