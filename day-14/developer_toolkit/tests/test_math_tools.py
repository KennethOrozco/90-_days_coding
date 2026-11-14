from toolkit import calculate_average, find_max

def test_average_multiple() -> None:
    assert calculate_average([10, 20, 30]) == 20.0

def test_average_single() -> None:
    assert calculate_average([3]) == 3.0

def test_average_empty() -> None:
    assert calculate_average([]) == 0.0

def test_max_positive() -> None:
    assert find_max([2,3,4,5]) == 5.0

def test_max_negative() -> None:
    assert find_max([-2, -3, -4, -5]) == -2.0

def test_max_empty():
    assert find_max([]) is None