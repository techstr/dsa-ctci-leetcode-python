import pytest


class Solution:
    """
    A class containing a method to calculate the factorial of a given number.

    Methods
    -------
    factorial(n: int) -> int
        Computes the factorial of a non-negative integer n.
        Returns 1 if n is 0, otherwise returns n * factorial(n-1).
    """

    # Recursion solution
    def factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


@pytest.mark.parametrize(
    "input_value, expected",
    [
        (0, 1),  # Factorial of 0
        (1, 1),  # Factorial of 1
        (2, 2),  # Factorial of 2
        (3, 6),  # Factorial of 3
        (4, 24),  # Factorial of 4
        (5, 120),  # Factorial of 5
    ],
)
def test_factorial_positive(input_value, expected):
    solution = Solution()
    assert solution.factorial(input_value) == expected
