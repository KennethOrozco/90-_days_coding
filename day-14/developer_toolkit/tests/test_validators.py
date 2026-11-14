from toolkit import is_valid_age, is_valid_email

def test_valid_age() -> None:
    assert is_valid_age(100)

def test_negative_age() -> None:
    assert not is_valid_age(-5)

def test_age_above_limit() -> None:
    assert not is_valid_age(150)

def test_valid_email() -> None:
    assert is_valid_email("Kenneth@gmail.com")

def test_missing_at() -> None:
    assert not is_valid_email("Kennethgmail.com")

def test_missing_domain() -> None:
    assert not is_valid_email("Kenneth@.")