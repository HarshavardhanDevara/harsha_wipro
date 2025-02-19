import pytest
def is_palindrome(strings):
    return strings == strings[::-1]

@pytest.mark.parametrize("strings,expected",[
    ("liril",True),
    ("malayalam",True),
    ("ada",True),
    ("lux",False)
])

def test_palindrome(strings,expected):
    assert is_palindrome(strings) == expected
