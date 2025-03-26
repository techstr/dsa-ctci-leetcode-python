# Description: A simple Python program to calculate the factorial of a non-negative integer
import pytest


def factorial(n):
    """Calculate the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer

    Returns:
        int: The factorial of n

    Raises:
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(f"Factorial of 5 is: {factorial(5)}")


def test_factorial_basic():
    """Test basic factorial calculations"""
    assert factorial(0) == 1, "Factorial of 0 should be 1"
    assert factorial(1) == 1, "Factorial of 1 should be 1"
    assert factorial(5) == 120, "Factorial of 5 should be 120"


def test_factorial_large():
    """Test a larger number"""
    assert factorial(10) == 3628800, "Factorial of 10 should be 3628800"


def test_factorial_negative():
    """Test that negative numbers raise ValueError"""
    with pytest.raises(ValueError, match="Input must be non-negative"):
        factorial(-1)


def test_factorial_non_integer():
    """Test that non-integers raise ValueError"""
    with pytest.raises(ValueError, match="Input must be an integer"):
        factorial(3.5)
