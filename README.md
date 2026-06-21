# Spoiler Detector

A Flask web app that uses the OpenAI API to classify movie review text as containing spoilers or not.

## Setup
```bash
pip install -r requirements.txt
```
Add your OpenAI key to `.env`:
```
OPENAI_API_KEY="your-key-here"
```
Run:
```bash
python app.py
```
Open `http://localhost:5001`.

## Files
- `app.py` – Flask server, serves the UI and `/check-spoiler` endpoint
- `spoiler_main.py` – calls OpenAI to classify text as Spoiler/Non-Spoiler
- `a.py` – simple CLI test script
- `test.py` – batch test script with sample reviews
- `templates/index.html` – front-end UI
- `datset/` – optional scripts to download (kagglehub) and train a local ML model on the IMDB spoiler dataset (separate from the OpenAI-based app)

## Bugs fixed
1. **`app.py`** – typo `'warxning'` → `'warning'`. This class didn't match any CSS rule in `index.html`, so spoiler results displayed with no styling/background color.
2. **`requirements.txt`** (replaced `req.txt` + `requirement.bash`, which were incomplete/inconsistent) – `flask` was missing entirely, so the app couldn't even start. Merged into one full, correct file.
3. **`datset/import kagglehub.py`** – called `df.head()` but `df` was never defined (`NameError`). Added the missing `pd.read_json(...)` load step.
4. Removed committed `__pycache__/` (build artifact, shouldn't be shipped).

## ⚠️ Security issue (action needed)
Your `.env` file contains a **live OpenAI API key** committed in this zip. Anyone with this file can use your key/billing.
- **Rotate/revoke this key now** at https://platform.openai.com/api-keys
- Keep using `.gitignore` (already correctly ignoring `.env`) but make sure you never zip/share the `.env` file itself.

## Notes (not bugs, just cleanup ideas)
- `importpanda.py` and `test.py` are leftover/duplicate scratch scripts not used by the app — fine to delete if unneeded.
- `importpanda.py` expects `spoiler_dataset.csv`, which isn't included.
