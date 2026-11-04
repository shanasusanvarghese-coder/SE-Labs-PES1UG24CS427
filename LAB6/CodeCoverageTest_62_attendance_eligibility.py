import pytest
from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning
)


def test_plain_percent():
    assert attendance_percent(30, 40, 0) == 75


def test_medical_leave_credit():
    assert attendance_percent(25, 40, 3) == 70


def test_medical_leave_capped_at_five():
    assert attendance_percent(20, 40, 8) == 62


def test_credit_cannot_exceed_total():
    assert attendance_percent(39, 40, 5) == 100


def test_invalid_total():
    with pytest.raises(ValueError):
        attendance_percent(10, 0, 0)


def test_negative_attendance():
    with pytest.raises(ValueError):
        attendance_percent(-1, 40, 0)


def test_attendance_greater_than_total():
    with pytest.raises(ValueError):
        attendance_percent(41, 40, 0)


def test_fees_pending():
    assert exam_eligibility(90, False, False) == "fees pending"


def test_eligible_without_condonation():
    assert exam_eligibility(80, False, True) == "eligible"


def test_eligible_with_condonation():
    assert exam_eligibility(70, True, True) == "eligible"


def test_condonation_required():
    assert exam_eligibility(70, False, True) == "condonation required"


def test_detained():
    assert exam_eligibility(60, True, True) == "detained"


def test_no_warning():
    assert attendance_warning(90, 2) is None


def test_reminder():
    assert attendance_warning(80, 2) == "reminder"


def test_critical_warning():
    assert attendance_warning(60, 5) == "critical"


def test_final_notice():
    assert attendance_warning(60, 3) == "final notice"
