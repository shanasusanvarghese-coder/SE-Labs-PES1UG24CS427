# LAB 7 — Fuzzing for Input Validation Bugs

**Project:** Attendance Eligibility Parser

This folder contains the fixed parser and Hypothesis property-based tests for the three input functions required by the LAB7 handout.

## Files

- `attendance_eligibility_parser.py` — input validation and parsing functions.
- `test_attendance_eligibility_parser.py` — Hypothesis fuzz tests and focused examples.
- `requirements.txt` — test dependencies.

## Behavior for invalid input

- `normalize_srn` returns an empty string for non-string values.
- `attendance_from_ratio` returns `None` for malformed ratios, zero/negative denominators, or impossible attendance counts.
- `attendance_from_register` returns `None` for non-string, empty, or non-P/A register values.

## Run locally

From this directory:

```bash
python3 -m pip install -r requirements.txt
python3 attendance_eligibility_parser.py
python3 -m pytest -q test_attendance_eligibility_parser.py
```

## Screenshot evidence still required

The handout requires four screenshots captured from actual terminal runs:

- **SS1:** original buggy application before replacing it.
- **SS2:** completed fuzz tests failing against the original buggy implementation.
- **SS3:** fixed application running with sample inputs.
- **SS4:** passing pytest summary for the fixed implementation.

SS1 and SS2 must be captured against the original starter code. They cannot truthfully be recreated from this fixed version. Capture SS3 and SS4 locally after running the commands above, then add the images to this folder.
