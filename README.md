# Equipment Logbook Parser

**Project:** Automated extraction and structuring of equipment health check records from unstructured maintenance logs.

**Focus:** Python automation · text processing · fuzzy matching · data cleaning · Excel reporting

---

## Project at a Glance

| Workstream | Core Challenge | Engineering Approach | Outcome |
|---|---|---|---|
| **P1 — Problem Definition** | Maintenance history is buried in free-text logs | Define the fields and output format needed for health check reviews | Clear extraction requirements |
| **P2 — Information Extraction** | Health check wording, spelling, and date placement vary | Combine keyword rules, fuzzy matching, and date association | Automatically identified candidate records |
| **P3 — Data Processing** | Extracted mentions need consistent labels and duplicate handling | Classify WS/RS components and consolidate date-component matches | Structured, reviewable records |
| **P4 — Reporting Automation** | Manual transcription makes historical reviews repetitive | Export standardized fields into formatted Excel | Reusable tabular output for further review |

---

## End-to-End System Overview

```mermaid
flowchart LR
    A["P1 · Define Data Requirements"] --> B["TXT Maintenance Log"]
    B --> C["P2 · Detect Health Check Mentions"]
    C --> D["Associate Dates"]
    D --> E["P3 · Classify WS / RS"]
    E --> F["Consolidate Records"]
    F --> G["P4 · Export Excel Report"]
```

**Storyline:** define useful maintenance fields → identify relevant text despite inconsistent wording → standardize and consolidate records → export a review-ready report.

---

## Project Details

### P1 — Problem Definition

> **Key Question —** How can scattered maintenance notes become consistent records without manual transcription?

**Highlights**
- Targeted health check mentions in plain-text equipment logbooks.
- Defined three consistent output fields: **check date, component type, and matched source text**.

**Impact:** Established a repeatable data format for reviewing historical maintenance mentions.

**Takeaway:** A small automation task becomes more useful when its outputs are defined before parsing begins.

### P2 — Information Extraction

> **Key Question —** How can relevant maintenance information be found when operators use inconsistent wording?

**Highlights**
- Combined direct keyword matching with **RapidFuzz** to recognize common spelling variations.
- Parsed supported date formats using **regular expressions**.
- Matched heading-style records to a following date and ordinary text entries to a preceding date.

**Impact:** Automated the identification of candidate health check entries that would otherwise require text-by-text searching.

**Takeaway:** Rule-based and approximate text matching can make semi-structured operational records easier to process.

### P3 — Data Processing

> **Key Question —** How can extracted text be converted into consistent, reviewable records?

**Highlights**
- Classified component mentions into **Wafer Stage (WS), Reticle Stage (RS), or Unknown**.
- Allowed one entry mentioning both components to produce separate WS and RS rows.
- Consolidated repeated matches using **check date + component type**, retaining the first match.

**Impact:** Converted heterogeneous logbook mentions into a common table layout suitable for sorting and follow-up review.

**Takeaway:** Standardization and explicit deduplication rules turn text matches into usable data, while preserving awareness of information that may be lost.

### P4 — Reporting Automation

> **Key Question —** How can extraction results be shared without repeatedly reformatting data?

**Highlights**
- Used **Pandas** to assemble and export records.
- Used **OpenPyXL** to preserve spreadsheet date formatting.
- Added command-line arguments for input file, output path, and fuzzy-match threshold.

**Impact:** Produced a repeatable Excel reporting workflow that separates source logbooks from structured output.

**Takeaway:** Practical data automation connects extraction logic to an output people can inspect and reuse.

---

## Key Engineering Takeaways

- **Workflow automation:** Turned manual logbook searching and record organization into a repeatable Python process.
- **Unstructured-to-structured data:** Combined text matching, date association, classification, and deduplication into one lightweight pipeline.
- **Operational usability:** Exported standardized Excel records that can support maintenance-history reviews and downstream analysis.

---

## Tech Stack

| Area | Technologies / Methods |
|---|---|
| **Programming** | Python |
| **Text Processing** | Regular Expressions · Text Normalization · RapidFuzz |
| **Data Processing** | Pandas · Component Classification · Deduplication |
| **Reporting** | OpenPyXL · Excel Export · CLI Arguments |

---

## Repository Structure

```text
.
├── README.md
├── logbook_parser.py
├── requirements.txt
├── .gitignore
└── examples/
    └── sample_logbook.txt
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the parser using synthetic example data:

```bash
python logbook_parser.py --input examples/sample_logbook.txt --output health_check_records.xlsx
```

The generated `health_checks` worksheet contains **Check Date**, **Health Check Type**, and **Matched Text**.

**Scope and limitations:** This is a focused portfolio example, not a validated maintenance audit or equipment tracking system. The script identifies health check *mentions*, not confirmed completed work; date association relies on the input layout; and date-component deduplication can suppress repeated events. No processing-time reduction or extraction-accuracy benchmark is claimed. All example data is synthetic; private maintenance records and proprietary information are excluded.
