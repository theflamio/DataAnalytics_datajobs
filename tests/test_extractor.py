# tests/test_calculator.py

def add_numbers(a, b):
    """
    Function to add two numbers.
    """
    return a + b

def test_add_numbers_integer():
    """
    Test case for adding two integer numbers.
    """
    assert add_numbers(1, 2) == 3
    assert add_numbers(5, 5) == 10
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
