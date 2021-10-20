import leons_functions

def test_alphabeta():
    assert leons_functions.alphabeta(5, 6, 7) == 7

def test_test_z():
    assert leons_functions.test_z(8) == ['Z was greater than 5',8]
    assert leons_functions.test_z(3) == ['Z was less than 5',3]