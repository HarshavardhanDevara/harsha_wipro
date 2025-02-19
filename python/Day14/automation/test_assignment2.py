import pytest 

def avg_list(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

@pytest.mark.parametrize("numbers,expected",[
    ([1,2,3,4,5],3.0),
    ([10,20,30],20.0),
    ([1],1.0),
    ([],0)
])

def test_avg(numbers,expected):
    assert avg_list(numbers) == expected
