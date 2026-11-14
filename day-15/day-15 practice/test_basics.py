def multiply(a: int, b: int) -> int:
    return a * b


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_first(items: list) -> object | None:
    if not items:
        return None
    return items[0]

def test_multiply_even() -> None:
    assert multiply(4, 5) == 20

def test_multiply_negative() -> None:
    assert multiply(-2, 6) == -12

def test_multipy_zero() -> None:
    assert multiply(4, 0) == 0

def test_is_even() -> None:
    assert is_even(8)

def test_is_not_even() -> None:
    assert not is_even(5)

def test_is_even_zero() -> None:
    assert  is_even(0) 

def test_get_first_int() -> None:
    assert get_first([1, 2, 3, 4, 5]) == 1

def test_get_first_str() -> None:
    assert get_first(["cat", "dog", "monkey"]) == "cat"

def test_get_first_empty() -> None:
    assert get_first([]) is None
