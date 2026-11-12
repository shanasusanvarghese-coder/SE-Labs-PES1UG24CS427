"""Input-safe attendance eligibility parsing helpers."""


def normalize_srn(srn):
    """Normalize an SRN; return an empty string for non-string input."""
    if not isinstance(srn, str):
        return ""
    return "".join(srn.split()).upper()


def attendance_from_ratio(text):
    """Convert 'ATTENDED/HELD' to an integer percentage.

    Return None when the input is malformed or the counts are impossible.
    """
    if not isinstance(text, str):
        return None

    parts = text.split("/")
    if len(parts) != 2:
        return None

    try:
        attended, held = (int(part.strip()) for part in parts)
    except (TypeError, ValueError):
        return None

    if held <= 0 or attended < 0 or attended > held:
        return None

    return attended * 100 // held


def attendance_from_register(marks):
    """Calculate the percentage of P marks in a P/A register.

    Return None for non-string, empty, or malformed registers.
    """
    if not isinstance(marks, str):
        return None

    normalized = marks.strip().upper()
    if not normalized or any(mark not in {"P", "A"} for mark in normalized):
        return None

    return normalized.count("P") * 100 // len(normalized)


def main():
    print("==== Running normalize_srn ====")
    value = input("Enter an SRN (e.g. pes1ug23cs001): ")
    print("Normalized SRN:", normalize_srn(value))

    print("\n==== Running attendance_from_ratio ====")
    value = input("Enter classes attended and held as ATTENDED/HELD (e.g. 30/40): ")
    print("Attendance percent:", attendance_from_ratio(value))

    print("\n==== Running attendance_from_register ====")
    value = input("Enter the register as P/A marks (e.g. PPAPP): ")
    print("Attendance percent:", attendance_from_register(value))


if __name__ == "__main__":
    main()
