import pytest
 
def Average(n_list):
    sum=0
    for i in n_list:
        sum=sum+i
    Avg=sum/len(n_list)
    return Avg

@pytest.mark.parametrize("n_list, expected", [
    ([1, 2, 3, 4, 5], 3.0),
    ([10, 20, 30], 20.0),
    ([1], 1.0),
    ([], 0)
])
 

def test_Average(n_list, expected):
    assert Average(n_list) == expected