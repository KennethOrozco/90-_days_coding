import pytest


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def test_division_even() -> None:
    assert divide(10, 2) == 5.0

def test_division_negative() -> None:
    assert divide(-10, 2) == -5.0

def test_division_zero() -> None:
    assert divide(0, 5) == 0

def test_division_odd() -> None:
    assert divide(7, 2) == 3.5

def test_division_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(10, 0)
