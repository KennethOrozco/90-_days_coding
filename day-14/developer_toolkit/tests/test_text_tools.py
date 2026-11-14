from toolkit import count_words, reverse_text

def test_count_normal() -> None:
    assert count_words("I love cats") == 3

def test_count_extra_spaces() -> None:
    assert count_words("    I am    a bird ") == 4

def test_count_empty() -> None:
    assert count_words("") == 0

def test_reverse_normal() -> None:
    assert reverse_text("hello") == "olleh"

def test_reverse_palindrome() -> None:
    assert reverse_text("radar") == "radar"

def test_reverse_empty() -> None:
    assert reverse_text("") == ""