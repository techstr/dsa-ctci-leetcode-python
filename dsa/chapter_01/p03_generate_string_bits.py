import pytest


class Solution:
    """
    Generate all the strings of n bits. Assume A[0..n – 1] is an array of size n.

    The following algorithm generates all the strings of n bits.
    1. Generate all the strings of n – 1 bits.
    2. For each string generated in step 1, append 0 to it and append 1 to it.
    3. Return all the strings generated in step 2.
    """

    def __init__(self, n: int):
        self.n = n
        self.result = []
        self.generate_strings("", n)

    def generate_strings(self, current: str, n: int) -> None:
        if n == 0:
            self.result.append(current)
            return
        self.generate_strings(current + "0", n - 1)
        self.generate_strings(current + "1", n - 1)


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["0", "1"]),
        (2, ["00", "01", "10", "11"]),
        (3, ["000", "001", "010", "011", "100", "101", "110", "111"]),
        (0, [""]),
    ],
)
def test_generate_strings(n, expected):
    solution = Solution(n)
    assert solution.result == expected
