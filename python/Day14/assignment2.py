import pytest
 
def Sum(n_list):
    sum=0
    for i in n_list:
        sum=sum+i
    return sum

@pytest.mark.parametrize("n_list, expected", [
    ([1, 2, 3, 4, 5], 15),
    ([10, 20, 30], 60),
    ([1], 1.0),
    ([], 0)
])
 

def test_Sum(n_list, expected):
    assert Sum(n_list) == expected