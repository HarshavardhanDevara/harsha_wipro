import pytest
 
def is_even(n):
    return n % 2 == 0
 
@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, False),
    (-4, True),
    (-5, False),
    (0, True)
])
 
 
def test_is_even(n, expected):
    assert is_even(n) == expected