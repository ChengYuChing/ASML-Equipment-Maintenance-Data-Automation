# Equipment Logbook Parser

**Project:** Turn text-based equipment maintenance logs into organized Excel records.

**Focus:** Python automation · text extraction · data cleaning · Excel reporting

---

## Project at a Glance

| Stage | Problem | What I Built | Result |
|---|---|---|---|
| **P1 — Define the Data** | Health check information is scattered across long text logs | Defined the date, component, and original text to capture | A consistent record format |
| **P2 — Find Health Checks** | The same activity can be written in different ways | Combined keyword matching, fuzzy matching, and date lookup | Health check mentions found automatically |
| **P3 — Organize Records** | Extracted text is inconsistent and may repeat | Classified WS/RS checks and removed repeated date–type matches | A clean, structured table |
| **P4 — Export Results** | Manual copying into spreadsheets takes extra work | Generated a formatted Excel report | Records ready to review and filter |

---

## End-to-End Workflow

```mermaid
flowchart LR
    A["TXT Maintenance Log"] --> B["Find Health Check Mentions"]
    B --> C["Match Dates"]
    C --> D["Classify WS / RS"]
    D --> E["Remove Repeated Matches"]
    E --> F["Excel Report"]
```

**In short:** read maintenance logs → find relevant entries → organize the information → export it to Excel.

---

## Project Details

### P1 — Define the Data

> **Question:** What information do we need from each maintenance entry?

Maintenance logs contain free-text notes rather than ready-to-use tables. I started by choosing three fields that make health check records easier to review:

- **Check Date:** When the log entry was recorded.
- **Health Check Type:** Wafer Stage (**WS**), Reticle Stage (**RS**), or Unknown.
- **Matched Text:** The original line that triggered extraction.

**Result:** Every extracted record follows the same format, making the output easier to sort and inspect.

### P2 — Find Health Checks

> **Question:** How do we find the same type of work when it is written differently?

- Used **keyword matching** to find standard phrases such as “health check.”
- Added **fuzzy matching (RapidFuzz)** to catch common spelling mistakes.
- Used **regular expressions** to read dates from the log.
- Linked a health check mention to a nearby date using rules based on the log layout.

**Result:** The script finds candidate health check records without manually searching each log entry.

### P3 — Organize Records

> **Question:** How do we turn matched lines into a consistent table?

- Identified **WS** and **RS** from abbreviations or full component names.
- Created separate rows when a line mentioned both components.
- Kept the first match for each **date + component type** combination.

**Result:** Text matches become structured records that are easier to review.

### P4 — Export Results

> **Question:** How do we make the extracted information usable?

- Used **Pandas** to organize the records.
- Used **OpenPyXL** to export dates and text to an Excel worksheet.
- Added command-line options to change the input file, output file, and matching threshold.

**Result:** A repeatable process produces an Excel report without manual copying and formatting.

---

## Key Engineering Takeaways

- **Automated repetitive work:** Replaced line-by-line searching and spreadsheet copying with a Python workflow.
- **Made text data usable:** Combined text matching, date lookup, and component classification to convert unstructured logs into a consistent table.
- **Built for practical review:** Delivered an Excel output that can be filtered, checked, and used in later maintenance analysis.

---

## Tech Stack

| Area | Tools & Methods |
|---|---|
| **Programming** | Python |
| **Text Extraction** | Regular Expressions · RapidFuzz |
| **Data Processing** | Pandas · Classification · Deduplication |
| **Reporting** | OpenPyXL · Excel |

---

## Repository Structure

```text
.
├── README.md
├── logbook_parser.py           # Main extraction script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Excludes generated and private files
└── examples/
    └── sample_logbook.txt     # Synthetic example data
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the script with the sample log:

```bash
python logbook_parser.py --input examples/sample_logbook.txt --output health_check_records.xlsx
```

The output is an Excel file with a `health_checks` sheet and three columns:

| Check Date | Health Check Type | Matched Text |
|---|---|---|
| 2026-01-15 | WS | WS Health Check |
| 2026-02-03 | RS | RS healthy check completed. |

*All example records are synthetic.*

---

## Scope & Limitations

This is a **small automation tool**, not a complete equipment monitoring system.

- The script finds **health check mentions**, which may include planned or canceled work.
- Date matching follows rules based on the log layout and may not work for every format.
- Multiple checks of the same component on the same date are merged into one row.
- Extraction accuracy and time savings have not been formally measured.

No internal maintenance logs or proprietary equipment data are included.
