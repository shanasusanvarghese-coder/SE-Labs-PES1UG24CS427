import pytest
from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning
)


@pytest.mark.parametrize("attended,total,medical,expected", [
    (30, 40, 0, 75),
    (25, 40, 3, 70),
    (20, 40, 8, 62),
    (39, 40, 5, 100),
    (0, 40, 0, 0),
    (40, 40, 0, 100),
])
def test_attendance_percent_valid(attended, total, medical, expected):
    assert attendance_percent(attended, total, medical) == expected


@pytest.mark.parametrize("attended,total,medical", [
    (10, 0, 0),
    (10, -1, 0),
    (-1, 40, 0),
    (41, 40, 0),
])
def test_attendance_percent_invalid(attended, total, medical):
    with pytest.raises(ValueError):
        attendance_percent(attended, total, medical)


@pytest.mark.parametrize("percent,condonation,fees,expected", [
    (80, False, False, "fees pending"),
    (80, False, True, "eligible"),
    (75, False, True, "eligible"),
    (70, True, True, "eligible"),
    (70, False, True, "condonation required"),
    (64, True, True, "detained"),
])
def test_exam_eligibility_branches(percent, condonation, fees, expected):
    assert exam_eligibility(percent, condonation, fees) == expected


@pytest.mark.parametrize("percent,weeks,expected", [
    (85, 2, None),
    (84, 2, "reminder"),
    (75, 2, "reminder"),
    (74, 5, "critical"),
    (74, 4, "final notice"),
])
def test_attendance_warning_branches(percent, weeks, expected):
    assert attendance_warning(percent, weeks) == expected
