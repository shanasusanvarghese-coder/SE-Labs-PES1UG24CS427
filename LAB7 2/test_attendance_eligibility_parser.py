"""Property-based tests for the attendance eligibility parser."""

from hypothesis import given, strategies as st

from attendance_eligibility_parser import (
    attendance_from_ratio,
    attendance_from_register,
    normalize_srn,
)


@given(st.text() | st.none())
def test_normalize_srn_no_crash(value):
    normalize_srn(value)


@given(st.text() | st.none())
def test_attendance_from_ratio_no_crash(value):
    attendance_from_ratio(value)


@given(st.text() | st.none())
def test_attendance_from_register_no_crash(value):
    attendance_from_register(value)


def test_normalize_srn_examples():
    assert normalize_srn(" pes1ug23 cs001 ") == "PES1UG23CS001"
    assert normalize_srn(None) == ""
    assert normalize_srn(" \t ") == ""


def test_attendance_from_ratio_examples():
    assert attendance_from_ratio("30/40") == 75
    assert attendance_from_ratio("0/10") == 0
    assert attendance_from_ratio("10/0") is None
    assert attendance_from_ratio("11/10") is None
    assert attendance_from_ratio("bad input") is None
    assert attendance_from_ratio(None) is None


def test_attendance_from_register_examples():
    assert attendance_from_register("PPAPP") == 80
    assert attendance_from_register("aaaa") == 0
    assert attendance_from_register("") is None
    assert attendance_from_register("PAX") is None
    assert attendance_from_register(None) is None
