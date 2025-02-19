value = 100
def test_greater():
    global value
    assert value > 100

def test_greater_equal():
    global value
    assert value == 100

def test_lower():
    global value
    assert value < 200 
