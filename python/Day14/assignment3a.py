import pytest
from assignment3 import check_anagram

@pytest.mark.parametrize("str1, str2, expected", [
    ("Listen", "Silent", "It is an Anagram (Using Sorting)"),
    ("Earth", "Heart", "It is an Anagram (Using Sorting)"),
    ("Astronomer", "Moonstarer", "It is an Anagram (Using Sorting)"),
    ("Hello", "World", "Not an Anagram"),
])
def test_check_anagram(str1, str2, expected):
    assert check_anagram(str1, str2) == expected
