# Task 3: Task Automation – Email Extractor

A small Python automation script that finds email addresses in a text file and writes the unique results to another text file.

## Files
- `extract_emails.py`: reads the input, extracts email addresses, and saves them.
- `sample_text.txt`: sample input file that you can edit or replace.
- `extracted_emails.txt`: generated output file (created when the script runs).

## Requirements
- Python 3
- No external packages

## Run
Keep `extract_emails.py` and `sample_text.txt` in the same folder, then run:
```bash
python extract_emails.py
```

## Concepts used
`re` (regular expressions), `pathlib`, file handling, functions, and sets.

## How it works
The script reads `sample_text.txt`, finds email-like strings using a regular expression, removes duplicates, sorts the results, and writes them to `extracted_emails.txt`.
