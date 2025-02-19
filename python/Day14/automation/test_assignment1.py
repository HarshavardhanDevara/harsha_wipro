import pytest 

def sum_of_list(numbers):
    if not numbers:
        return 0
    return sum(numbers)

@pytest.mark.parametrize("numbers,expected",[
    ([1,2,3,4,5],15),
    ([10,20,30],60),
    ([1],1.0),
    ([],0)
])

def test_sum(numbers,expected):
    assert sum_of_list(numbers) == expected