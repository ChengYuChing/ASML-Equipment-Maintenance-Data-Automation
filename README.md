# Equipment Logbook Parser

A lightweight Python tool for extracting equipment health check mentions from unstructured maintenance logs and exporting structured Excel records.

## Problem

Free-text maintenance logbooks are difficult to search and summarize consistently, especially when record wording and spelling vary. This project converts health check mentions into a tabular format for easier review.

## Approach

```text
TXT logbook
    ↓
Keyword detection + fuzzy matching
    ↓
Date association + WS / RS classification
    ↓
Date-component deduplication
    ↓
Excel report
```

## Key Features

- Detects common variants of "health check" using keyword rules and RapidFuzz.
- Classifies mentions as **Wafer Stage (WS)**, **Reticle Stage (RS)**, or **Unknown**.
- Associates dates by searching **below separator-delimited headings** or **above other matched lines**.
- Retains the first match for each date-component combination.
- Exports actual Excel date cells with readable date formatting.

## Tech Stack

**Python · Regular Expressions · RapidFuzz · Pandas · OpenPyXL**

## Quick Start

```bash
pip install -r requirements.txt
python logbook_parser.py --input examples/sample_logbook.txt --output health_check_records.xlsx
```

The command generates an Excel workbook with a `health_checks` sheet:

| Check Date | Health Check Type | Matched Text |
| --- | --- | --- |
| 2026-01-15 | WS | WS Health Check |
| 2026-02-03 | RS | RS healthy check completed. |
| 2026-03-20 | Unknown | Health check completed; component not specified. |
| 2026-04-11 | WS | WS and RS health check completed. |
| 2026-04-11 | RS | WS and RS health check completed. |

All example data is synthetic.

## Project Structure

```text
equipment-logbook-parser/
├── README.md
├── logbook_parser.py
├── requirements.txt
├── .gitignore
└── examples/
    └── sample_logbook.txt
```

## Limitations

- This tool identifies **mentions**, not verified completed maintenance events. Scheduled or canceled checks may also match.
- Date association assumes a particular logbook layout and may misattribute records in other formats.
- The first same-date, same-component match is retained; repeated events may be lost.
- The parser processes one TXT file per run. Matching accuracy has not been benchmarked.

## Data & Privacy

This standalone portfolio example uses synthetic logs only. Do not upload internal maintenance records, asset identifiers, customer data, or proprietary code without authorization.
