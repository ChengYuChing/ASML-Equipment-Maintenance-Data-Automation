"""Extract health check mentions from plain-text equipment maintenance logs.

This standalone portfolio example uses synthetic data and generic terminology.
It is not a verified maintenance-event audit tool.
"""

import argparse
import re
from datetime import datetime
from pathlib import Path

import pandas as pd
from rapidfuzz import fuzz

DATE_REGEX = re.compile(
    r"^\s*Date\s*[:\-]\s*(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\s*$",
    re.IGNORECASE,
)
SEP_REGEX = re.compile(r"^\s*[=\-]{6,}\s*$")
WS_REGEX = re.compile(r"(?<!\w)ws(?!\w)|\bwafer\s*stage\b", re.IGNORECASE)
RS_REGEX = re.compile(r"(?<!\w)rs(?!\w)|\breticle\s*stages?\b", re.IGNORECASE)

HEALTH_CHOICES = (
    "health check", "healthy check", "health  check", "haelth check",
    "heath check", "healthcheck", "healthy ckeck", "health ckeck",
    "haelthy chek", "healty check",
    "wafer stage health check", "reticle stage health check",
    "wafer stage healthy check", "reticle stage healthy check",
)


def normalize(value: str) -> str:
    return " ".join(value.lower().split())


def is_health_line(line: str, threshold: int) -> bool:
    text = normalize(line)
    if any(phrase in text for phrase in HEALTH_CHOICES):
        return True
    return fuzz.partial_ratio(text, "health check") >= threshold


def extract_types(line: str) -> list[str]:
    types = []
    if WS_REGEX.search(line):
        types.append("WS")
    if RS_REGEX.search(line):
        types.append("RS")
    return types or ["Unknown"]


def extract_date(line: str):
    match = DATE_REGEX.match(line)
    if not match:
        return None
    for fmt in ("%m/%d/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(match.group(1), fmt)
        except ValueError:
            continue
    return None


def parse_logbook(text: str, threshold: int = 88) -> pd.DataFrame:
    """Match health check mentions to dates using the original logbook heuristic.

    A heading between separators searches downward for its date. Other lines
    search upward. Records with no matching date are omitted. On the same
    date and component, only the first matching mention is retained.
    """
    lines = text.splitlines()
    records = []

    for index, line in enumerate(lines):
        if not is_health_line(line, threshold):
            continue

        is_heading = (
            0 < index < len(lines) - 1
            and SEP_REGEX.fullmatch(lines[index - 1]) is not None
            and SEP_REGEX.fullmatch(lines[index + 1]) is not None
        )
        indices = (
            range(index + 1, len(lines)) if is_heading else range(index - 1, -1, -1)
        )
        record_date = next(
            (date for j in indices if (date := extract_date(lines[j])) is not None),
            None,
        )
        if record_date is None:
            continue

        for component in extract_types(line):
            records.append({
                "Check Date": record_date,
                "Health Check Type": component,
                "Matched Text": line.strip(),
            })

    columns = ["Check Date", "Health Check Type", "Matched Text"]
    if not records:
        return pd.DataFrame(columns=columns)
    return pd.DataFrame(records, columns=columns).drop_duplicates(
        subset=["Check Date", "Health Check Type"], keep="first"
    ).reset_index(drop=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract health check mentions from a TXT logbook.")
    parser.add_argument("--input", type=Path, default=Path("examples/sample_logbook.txt"))
    parser.add_argument("--output", type=Path, default=Path("health_check_records.xlsx"))
    parser.add_argument("--threshold", type=int, default=88)
    args = parser.parse_args()
    if not 0 <= args.threshold <= 100:
        parser.error("--threshold must be between 0 and 100")

    text = args.input.read_text(encoding="utf-8")
    df = parse_logbook(text, threshold=args.threshold)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(args.output, engine="openpyxl", datetime_format="mm/dd/yyyy") as writer:
        df.to_excel(writer, index=False, sheet_name="health_checks")
        worksheet = writer.sheets["health_checks"]
        for cell in worksheet["A"][1:]:
            cell.number_format = "mm/dd/yyyy"

    print(f"Exported {len(df)} records to {args.output}")


if __name__ == "__main__":
    main()
