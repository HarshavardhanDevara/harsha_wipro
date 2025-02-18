import pytest
 
def is_palindrome(str1):
    return str1==str1[::-1]

@pytest.mark.parametrize("str1, expected", [
    ('liril' , True),
    ('malayalam', True),
    ('ada', True),
    ('lux', False)
])
 

def test_is_palindrome(str1, expected):
    assert is_palindrome(str1) == expected