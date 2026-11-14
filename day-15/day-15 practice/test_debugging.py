import pytest 

def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100!")

    return price - (price * discount / 100)

def test_normal_discount() -> None:
    assert calculate_discount(100, 20) == 80.0

def test_no_discount() -> None:
    assert calculate_discount(100, 0) == 100.0

def test_full_discount() -> None:
    assert calculate_discount(100, 100) == 0.0

def test_invalid_discount() -> None:
    with pytest.raises(ValueError):
        calculate_discount(100, 150)
        
