# Equipment Logbook Parser

**Project:** Python automation for turning unstructured equipment maintenance logs into organized health check records.

**Focus:** Text extraction · fuzzy matching · data cleaning · Excel reporting

---

## Project at a Glance

| Workstream | Core Challenge | Engineering Response | Outcome |
|---|---|---|---|
| **[P1 — Problem Definition](#p1--problem-definition)** | Years of maintenance notes are difficult to search and compare | Defined essential fields for health check tracking | A consistent record structure |
| **[P2 — Record Extraction](#p2--record-extraction)** | Different wording and date layouts make manual searches unreliable | Combined keyword rules, fuzzy matching, and date lookup | Automatically identified health check mentions |
| **[P3 — Data Standardization](#p3--data-standardization)** | Raw matches use different component names and can repeat | Classified WS/RS checks and consolidated repeated date–type matches | A structured, reviewable dataset |
| **[P4 — Report Automation](#p4--report-automation)** | Turning log notes into spreadsheets requires repetitive manual work | Built a Python-to-Excel export workflow | Reusable records for maintenance-history reviews |

---

## End-to-End System Overview

```mermaid
flowchart LR
    A["Text Maintenance Logs"] --> B["P2 · Extract Health Check Mentions"]
    B --> C["Find Associated Dates"]
    C --> D["P3 · Standardize WS / RS Records"]
    D --> E["Remove Repeated Matches"]
    E --> F["P4 · Export Excel Report"]
```

**Storyline:** define useful fields → extract relevant maintenance mentions → standardize the records → export results for review.

---

## Key Engineering Takeaways

- **Workflow automation:** Replaced manual searching and spreadsheet transcription with a reusable Python script.
- **Unstructured data processing:** Linked fuzzy text matching, date lookup, classification, and duplicate handling in one pipeline.
- **Practical output:** Produced structured Excel records that support faster inspection and future analysis.


---

## Project Details

### P1 — Problem Definition

> **Key Question —** How can scattered maintenance notes be turned into records that are easy to review?

#### 1. Highlights

- **Problem framing** — identified the manual work involved in finding health check entries across text-based logs.
- **Data requirements** — defined three output fields: **check date, component type, and matched source text**.

#### 2. Impact

- Established a consistent data format for **text extraction → record cleaning → Excel reporting**.

#### 3. Key Takeaway

> Defining the output first made each processing step serve a clear purpose: easier review of maintenance history.

#### 4. Next

**P2 → Record Extraction:** Find health check entries even when wording and spelling vary.

---

### P2 — Record Extraction

> **Key Question —** How can the script find health checks written in different ways?

#### 1. Highlights

- **Flexible text matching** — combined keyword rules and **RapidFuzz** to catch common spelling variations.
- **Date association** — used regular expressions and simple layout rules to connect each match to a nearby date.

#### 2. Impact

- Automated the search for health check mentions, replacing repetitive line-by-line lookup with a repeatable process.

#### 3. Key Takeaway

> Combining exact and approximate matching helps extract useful information from inconsistent operational notes.

#### 4. Next

**P3 → Data Standardization:** Turn matched text into consistent WS/RS records and handle repeated matches.

---

### P3 — Data Standardization

> **Key Question —** How can raw text matches become a consistent dataset?

#### 1. Highlights

- **Component classification** — recognized **Wafer Stage (WS)** and **Reticle Stage (RS)** using abbreviations or full names.
- **Record consolidation** — separated entries that mention both components and kept the first match for each **date + component** pair.

#### 2. Impact

- Converted scattered text matches into a structured table that can be **sorted, filtered, and reviewed**.

#### 3. Key Takeaway

> Standardized labels and clear duplicate rules make extracted records easier to use, although repeat events on the same day may be lost.

#### 4. Next

**P4 → Report Automation:** Export the structured records into an Excel report.

---

### P4 — Report Automation

> **Key Question —** How can the extracted records be delivered without manual spreadsheet work?

#### 1. Highlights

- **Automated reporting** — used **Pandas and OpenPyXL** to produce Excel files with properly formatted dates.
- **Reusable execution** — added command-line options for input file, output file, and matching threshold.

#### 2. Impact

- Built a repeatable **TXT → structured records → Excel** workflow for maintenance-history reviews.

#### 3. Key Takeaway

> A useful automation project connects data extraction to a simple output that people can inspect and reuse.

#### 4. Next

**Potential improvements:** Validate extraction accuracy and support additional log layouts before using the results for maintenance decisions.

---


## Tech Stack

| Area | Technologies / Methods |
|---|---|
| **Programming** | Python |
| **Text Extraction** | Regular Expressions · RapidFuzz |
| **Data Processing** | Pandas · Classification · Deduplication |
| **Reporting** | OpenPyXL · Excel · Command-Line Arguments |

---

## Portfolio Note

This repository is a **project overview only**. Implementation files, internal maintenance data, and runnable examples are intentionally not published. The description summarizes the engineering approach without providing proprietary source code.

**Scope and limitations:** The workflow identifies health check mentions rather than verifying completed maintenance events. Date matching depends on log layout, and date-component deduplication can suppress repeated events. Extraction accuracy and time savings have not been formally benchmarked.
